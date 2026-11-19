# Video and submission guide (3–7 minutes)

**Before recording:** Start MySQL, run `python app.py`, open http://127.0.0.1:5000/, and open Workbench with `job_tracker`. Prepare non-sensitive sample records. Use Windows Snipping Tool screen recording, macOS QuickTime screen recording, or OBS. Save as `demo.mp4` if supported.

Suggested 5-minute walkthrough:
1. **0:00–0:35** — Introduce CareerTrack; show dashboard and navigation.
2. **0:35–1:25** — Companies: create a sample company, open detail, edit, and show list.
3. **1:25–2:15** — Jobs: add a job for that company, including `Python, SQL, Flask` requirements; edit and view it.
4. **2:15–3:05** — Applications and contacts: add one of each, show status and interview JSON, edit one. Show delete confirmation with a temporary record; do not delete parent records while children exist.
5. **3:05–3:50** — Job Match: enter `Python, SQL`; show the match percentage and missing skill `flask`. Explain matched requirements / total requirements.
6. **3:50–4:30** — Switch to MySQL Workbench: show `job_tracker` tables, foreign keys, JSON columns and execute `SELECT * FROM jobs;` and `SELECT * FROM applications;`.
7. **4:30–5:00** — Show terminal running Flask, project file structure in VS Code, and README setup steps. Wrap up.

Check that your recording shows **client (browser), server (Flask terminal), and database (Workbench)**. Review audio/video playback, upload the actual video file to GitHub, then test that the repository is accessible. The instructor states missing video means the project will not be graded.
