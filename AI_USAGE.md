# AI Usage Documentation — COP4751

## Tools used
- **ChatGPT (GPT-6)**: Assisted with planning, generating initial Flask routes, SQL schema, HTML templates, CSS, validation, and setup documentation for the Job Application Tracker.

## Key prompts (actual requests, paraphrased for readability)
- “Can you make the project based on Assignments 1–5?”
- “Get the project done and tell me what I need to do for the video and where to put the code.”

## What AI generated
- Four-table MySQL schema with primary/foreign keys, JSON columns and indexes.
- Flask CRUD route scaffolding and reusable parameterized database helpers.
- Dashboard, forms, lists, details, styling, and a skills-match algorithm.
- Setup and demonstration guides.

## What worked well
- Shared metadata for CRUD routes reduces repeated code.
- Parameterized queries help avoid SQL injection in form values.
- A single reusable matching function normalizes case and whitespace.

## What I changed / tested personally
**Complete this section truthfully after running the project.** Describe your actual changes, any errors encountered, fixes you made, and which CRUD and matching flows you personally tested. Do not claim tests or modifications that you did not perform.

## Lessons learned
**Complete in your own words after using the application.** Suggested topics: MySQL foreign-key dependencies, storing arrays in JSON, Flask request handling, interpreting errors, and the importance of testing AI-generated code.

## Verification checklist
- [ ] Tested database creation on my own MySQL installation
- [ ] Tested create/read/update/delete on all four tables
- [ ] Tested matching percentage and missing skills
- [ ] Verified fresh-clone setup instructions
- [ ] Recorded and uploaded demo video

> This file documents AI assistance; review and update it before submission so it accurately reflects your own workflow.
