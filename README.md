CareerTrack — COP4751 Job Application Tracker

A Flask + MySQL web application that implements the CRUD functionality of companies, jobs, applications, contacts**, dashboard, and job matching via skills. Built based on the provided COP4751 course project specification and Assignments 1–5.

Requirements
- Python version 3.10+; MySQL Server 8.0+; optional MySQL Workbench for creating schema; optional Git for local use.

Fresh-clone setup
1. Clone using `git clone https://github.com/jovanilic46/job-application-tracker.git` then `cd job-application-tracker` (alternatively, you may extract/unzip this project and use its folder in VS Code).
2. Create an environment using `python -m venv .venv`.
3. Activate your environment via PowerShell with `.\.venv\Scripts\Activate.ps1` or with `source .venv/bin/activate`. If you cannot use `ps1` files, just use `.venv\Scripts\python.exe` directly in commands below instead.
4. Install dependencies with `python -m pip install -r requirements.txt`.
5. Open **MySQL Workbench**; connect to your MySQL Server (use localhost and user=root if developing locally); and execute `schema.sql` file (click on lightning bolt).
The script creates `job_tracker` database and four tables. **It doesn’t populate sample data or drop any tables.**
6. Copy `.env.example` to `.env` and configure your `DB_PASSWORD`, `DB_USER` and `FLASK_SECRET_KEY`. Keep `.env` secret. For local development only, `root` username can be used. Use limited DB account in production.
7. Run with `python app.py`; go to **http://127.0.0.1:5000/**
8. Add a company, a job with comma-separated requirements, an application and/or contact; go to Job Match and type skills like `Python, SQL, Flask`

Features and behavior
- CRUD with server-side validation and delete confirmation; parents cannot be deleted with dependent records.
- `requirements` stores JSON array of normalized skill strings; `interview_data` – JSON dictionary.
- The match % = matched required skills/total required skills * 100, truncated. Jobs without required skills will show up as 0%. Matching ignores case and requires an exact match; sorted by descending order.
- Parameterized SQL values; foreign keys; indexes and MySQL transactions; rolling back transaction in case of errors.
- No user accounts or deployment; built for local course project demostration.

Possible troubleshooting
- `Access denied for user 'root'@'%'` – wrong MySQL credentials in `.env`
- Can't connect – start MySQL Server and set correct `DB_HOST`
- `Unknown database` – execute `schema.sql` in MySQL Workbench.
- `ModuleNotFoundError` – activate environment and install packages again.
- There are no jobs in the dropdown – add at least one company and job.

GitHub submission
Create `job-application-tracker` repository on GitHub; upload all files/folders from project root (excluding ZIP containing the folder; don't upload anything else) including `templates/`, `static/`, `schema.sql`, `app.py`, `database.py`, `README.md`, `AI_USAGE.md` and `requirements.txt`. **Do not upload `.env`, `.venv` or your password.**
Also add the recorded **3–7 minute demo video** (i.e. `demo.mp4`). GitHub file-size restrictions apply for web uploading; use Git LFS as allowed by the instructor. Verify the instructor could retrieve video file from repository (cloning). Make commits with descriptive messages. Submit the URL.

Demo plan
See `VIDEO_GUIDE.md` for details on how to record demo video. Show browser, terminal where you run Flask, and MySQL Workbench. Make sure that everything works and only record.