"""COP4751 Job Application Tracker: Flask CRUD + skills matching."""
import json
import os
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from mysql.connector import Error, IntegrityError
from database import query, execute

app=Flask(__name__)
app.secret_key=os.getenv('FLASK_SECRET_KEY','local-dev-only-change-this')

TABLES={
 'companies': {'pk':'company_id','title':'Companies','fields':[('company_name','Company name','text',True),('industry','Industry','text',False),('website','Website','url',False),('city','City','text',False),('state','State','text',False),('notes','Notes','textarea',False)]},
 'jobs': {'pk':'job_id','title':'Jobs','fields':[('company_id','Company','company',True),('job_title','Job title','text',True),('job_type','Job type','job_type',False),('salary_min','Minimum salary','number',False),('salary_max','Maximum salary','number',False),('job_url','Job URL','url',False),('date_posted','Date posted','date',False),('requirements','Required skills (comma separated)','skills',False)]},
 'applications': {'pk':'application_id','title':'Applications','fields':[('job_id','Job','job',True),('application_date','Application date','date',True),('status','Status','status',True),('resume_version','Resume version','text',False),('cover_letter_sent','Cover letter sent','checkbox',False),('interview_data','Interview details (JSON object)','json',False)]},
 'contacts': {'pk':'contact_id','title':'Contacts','fields':[('company_id','Company','company',True),('contact_name','Contact name','text',True),('title','Title','text',False),('email','Email','email',False),('phone','Phone','text',False),('linkedin_url','LinkedIn URL','url',False),('notes','Notes','textarea',False)]}
}
JOB_TYPES=['Full-time','Part-time','Contract','Internship']
STATUSES=['Applied','Screening','Interview','Offer','Rejected','Withdrawn']

@app.context_processor
def globals_for_templates(): return {'sections':TABLES}

@app.route('/')
def dashboard():
    counts={t:query(f'SELECT COUNT(*) AS n FROM {t}',one=True)['n'] for t in TABLES}
    statuses=query('SELECT status,COUNT(*) AS n FROM applications GROUP BY status ORDER BY n DESC')
    recent=query("""SELECT a.application_id,a.application_date,a.status,j.job_title,c.company_name FROM applications a JOIN jobs j ON a.job_id=j.job_id JOIN companies c ON j.company_id=c.company_id ORDER BY a.application_date DESC,a.application_id DESC LIMIT 8""")
    return render_template('dashboard.html',counts=counts,statuses=statuses,recent=recent)

def options_for(fields):
    options={}
    if any(f[2]=='company' for f in fields): options['company']=query('SELECT company_id AS id,company_name AS name FROM companies ORDER BY company_name')
    if any(f[2]=='job' for f in fields): options['job']=query("""SELECT j.job_id AS id, CONCAT(j.job_title,' — ',c.company_name) AS name FROM jobs j JOIN companies c ON j.company_id=c.company_id ORDER BY c.company_name,j.job_title""")
    return options

def normalized_skills(value):
    if isinstance(value,list): items=value
    elif isinstance(value,dict): items=value.get('skills',[])
    elif isinstance(value,str):
        try:
            parsed=json.loads(value)
            if isinstance(parsed,(list,dict)): return normalized_skills(parsed)
        except (ValueError,TypeError): pass
        items=value.split(',')
    else: items=[]
    return list(dict.fromkeys(str(s).strip().lower() for s in items if str(s).strip()))

def parse_form(section):
    values={}
    for key,label,kind,required in TABLES[section]['fields']:
        raw=request.form.get(key,'').strip()
        if kind=='checkbox': values[key]=1 if request.form.get(key) else 0; continue
        if required and not raw: raise ValueError(f'{label} is required.')
        if kind in ('company','job','number'):
            if raw and (not raw.isdigit() or (kind in ('company','job') and int(raw)<1)): raise ValueError(f'{label} must be a valid nonnegative integer.')
            values[key]=int(raw) if raw else None
        elif kind=='skills': values[key]=json.dumps(normalized_skills(raw))
        elif kind=='json':
            if raw:
                try: obj=json.loads(raw)
                except ValueError: raise ValueError('Interview details must be valid JSON.')
                if not isinstance(obj,dict): raise ValueError('Interview details must be a JSON object.')
                values[key]=json.dumps(obj)
            else: values[key]=None
        elif kind in ('job_type','status'):
            allowed=JOB_TYPES if kind=='job_type' else STATUSES
            if raw and raw not in allowed: raise ValueError(f'Invalid {label}.')
            values[key]=raw or None
        else: values[key]=raw or None
    if section=='jobs' and values['salary_min'] is not None and values['salary_max'] is not None and values['salary_min']>values['salary_max']: raise ValueError('Minimum salary cannot exceed maximum salary.')
    return values

@app.route('/<section>')
def list_records(section):
    if section not in TABLES: abort(404)
    pk=TABLES[section]['pk']
    if section=='jobs': sql='SELECT j.*,c.company_name FROM jobs j JOIN companies c ON j.company_id=c.company_id ORDER BY j.job_id DESC'
    elif section=='applications': sql='SELECT a.*,j.job_title,c.company_name FROM applications a JOIN jobs j ON a.job_id=j.job_id JOIN companies c ON j.company_id=c.company_id ORDER BY a.application_id DESC'
    elif section=='contacts': sql='SELECT x.*,c.company_name FROM contacts x JOIN companies c ON x.company_id=c.company_id ORDER BY x.contact_id DESC'
    else: sql='SELECT * FROM companies ORDER BY company_id DESC'
    return render_template('list.html',section=section,config=TABLES[section],records=query(sql))

@app.route('/<section>/new',methods=['GET','POST'])
def create_record(section):
    if section not in TABLES: abort(404)
    cfg=TABLES[section]
    if request.method=='POST':
        try:
            values=parse_form(section); cols=list(values)
            execute(f"INSERT INTO {section} ({','.join(cols)}) VALUES ({','.join(['%s']*len(cols))})",tuple(values.values()))
            flash('Record created successfully.','success');return redirect(url_for('list_records',section=section))
        except (ValueError,Error) as exc: flash(str(exc),'error')
    return render_template('form.html',section=section,config=cfg,record={},options=options_for(cfg['fields']),types=JOB_TYPES,statuses=STATUSES,editing=False)

@app.route('/<section>/<int:record_id>')
def detail_record(section,record_id):
    if section not in TABLES: abort(404)
    cfg=TABLES[section];record=query(f"SELECT * FROM {section} WHERE {cfg['pk']}=%s",(record_id,),one=True)
    if not record: abort(404)
    return render_template('detail.html',section=section,config=cfg,record=record)

@app.route('/<section>/<int:record_id>/edit',methods=['GET','POST'])
def edit_record(section,record_id):
    if section not in TABLES: abort(404)
    cfg=TABLES[section];record=query(f"SELECT * FROM {section} WHERE {cfg['pk']}=%s",(record_id,),one=True)
    if not record: abort(404)
    if request.method=='POST':
        try:
            values=parse_form(section);cols=list(values)
            execute(f"UPDATE {section} SET {','.join(c+'=%s' for c in cols)} WHERE {cfg['pk']}=%s",tuple(values.values())+(record_id,))
            flash('Record updated.','success');return redirect(url_for('list_records',section=section))
        except (ValueError,Error) as exc: flash(str(exc),'error')
    return render_template('form.html',section=section,config=cfg,record=record,options=options_for(cfg['fields']),types=JOB_TYPES,statuses=STATUSES,editing=True)

@app.route('/<section>/<int:record_id>/delete',methods=['POST'])
def delete_record(section,record_id):
    if section not in TABLES: abort(404)
    cfg=TABLES[section]
    try:
        execute(f"DELETE FROM {section} WHERE {cfg['pk']}=%s",(record_id,))
        flash('Record deleted.','success')
    except IntegrityError: flash('Cannot delete: related records exist. Delete dependent records first.','error')
    except Error as exc: flash(f'Database error: {exc}','error')
    return redirect(url_for('list_records',section=section))

@app.route('/job-match',methods=['GET','POST'])
def job_match():
    raw=request.form.get('skills','') if request.method=='POST' else ''
    skills=normalized_skills(raw); results=[]
    if request.method=='POST':
        if not skills: flash('Enter at least one skill.','error')
        else:
            jobs=query('SELECT j.job_id,j.job_title,j.requirements,c.company_name FROM jobs j JOIN companies c ON j.company_id=c.company_id')
            for job in jobs:
                required=normalized_skills(job['requirements'])
                matched=sorted(set(required)&set(skills));missing=sorted(set(required)-set(skills))
                # Percentage of job requirements met, not percentage of user skills used.
                pct=round(len(matched)/len(required)*100) if required else 0
                results.append({**job,'percentage':pct,'matched':matched,'missing':missing,'total':len(required)})
            results.sort(key=lambda j:(-j['percentage'],-len(j['matched']),j['job_title'].lower()))
    return render_template('match.html',skills=raw,results=results)

if __name__=='__main__': app.run(debug=True)
