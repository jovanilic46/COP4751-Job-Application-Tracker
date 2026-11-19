# CareerTrack — COP4751 Job Application Tracker

A Flask + MySQL web app implementing CRUD for **companies, jobs, applications, contacts**, a dashboard, and a skills-based job matching page. Based on the provided COP4751 course project specification and Assignments 1–5.

## Requirements
- Python 3.10+; MySQL Server 8.0+; MySQL Workbench recommended; Git optional for local use.

## Fresh-clone setup
1. Clone: `git clone https://github.com/YOUR_USERNAME/job-application-tracker.git` then `cd job-application-tracker` (or unzip this project and open its folder in VS Code).
2. Create environment: `python -m venv .venv`.
3. Activate: Windows PowerShell `.venv\Scripts\Activate.ps1`; macOS/Linux `source .venv/bin/activate`. If PowerShell blocks activation, use `.venv\Scripts\python.exe` directly in later commands.
4. Install: `python -m pip install -r requirements.txt`.
5. Open **MySQL Workbench**, connect to your local MySQL server, open `schema.sql`, and execute the entire file (lightning bolt). It creates `job_tracker` and four tables. **It does not insert sample data or delete existing records.**
6. Copy `.env.example` to `.env` and set your own `DB_PASSWORD`, `DB_USER`, and a random `FLASK_SECRET_KEY`. Keep `.env` private; never upload it to GitHub. For local development only, the default user is root. Use a restricted DB account in production.
7. Start: `python app.py`. Open **http://127.0.0.1:5000/**.
8. Add a company first, then a job with comma-separated requirements, then an application and/or contact. Visit Job Match and enter skills such as `Python, SQL, Flask`.

## Features and behavior
- CRUD with server-side validation and confirmation on delete; parent records cannot be deleted while dependent records exist.
- `requirements` is stored as a JSON array of normalized skill strings; `interview_data` is a JSON object.
- Job Match percentage = matched required skills / total required skills × 100, rounded to whole percent. Jobs with no required skills show 0% (not 100%). Case-insensitive exact skill matching; results sorted highest first.
- Parameterized SQL values; MySQL foreign keys, indexes, and transactions with rollback on errors.
- No user accounts or production deployment; intended for local coursework demonstration.

## Troubleshooting
- `Access denied`: check MySQL credentials in `.env`.
- `Can't connect`: start MySQL Server and check `DB_HOST`.
- `Unknown database`: run `schema.sql` in Workbench.
- `ModuleNotFoundError`: activate venv and reinstall requirements.
- No jobs in dropdown: create a company and job first.

## GitHub submission
Create a repository named `job-application-tracker` on GitHub. Upload all files/folders from this project root (not the containing ZIP), including `templates/`, `static/`, `schema.sql`, `app.py`, `database.py`, `README.md`, `AI_USAGE.md`, and `requirements.txt`. Do **not** upload `.env`, `.venv`, or your database password. Add your recorded **3–7 minute demo video** (e.g. `demo.mp4`) to the repository root. GitHub web uploads have file-size limits; for larger videos use Git LFS if permitted by the instructor, and verify the instructor can access the actual video file after cloning. Commit regularly with descriptive messages and submit the repository URL.

## Demo plan
See `VIDEO_GUIDE.md`. Record the browser, terminal showing Flask running, and MySQL Workbench showing tables/rows. Verify all three before recording.
