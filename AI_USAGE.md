AI Usage Documentation — COP4751

Project name: Job Application Tracker (CareerTrack)

AI tool: ChatGPT (GPT-6)

1. Tools used

ChatGPT (GPT-6) was used for generating a code and helping me to develop a code for Job Application Tracker.

My Job Application Tracker was created using such tools and technologies as Python, Flask, MySQL, HTML and CSS.

As the development environment, I used Visual Studio Code and GitHub for the version controlling.

2. Main prompts

Some of the prompts and requests made to ChatGPT include:

"Can you make the project based on Assignments 1–5?"

"Get the project done and tell me what I need to do for the video and where to put the code"

"Help me configure MySQL and connect it to my Flask application"

"Why am I getting an unknown column error when running my Flask application?"

"Test the CRUD functionality and the job-matching feature"

"Guide me on how to upload my project on GitHub"

These are the key topics where I needed some help with.

3. What has been generated

AI assistance from ChatGPT helped me generate the project structure and its elements such as:

- MySQL database that includes four related tables: companies, jobs, applications and contacts

- Primary keys, foreign keys, JSON and other columns

- The initial set of Flask routes for creating, retrieving, updating and deleting records

- Functionality of connecting to a database and running some queries 

- Some basic HTML templates and CSS styles 

- The dashboard with application's statistic and recent activities 

- The algorithm calculating a matching percentage between users' skills and job requirements

- Initial setup instructions and project documentation

4. What has been working well

ChatGPT worked best in generating an initial structure of my application and reducing my repetitive coding.

The generated Flask routes and database functions provided a good starting point to connect frontend to MySQL. Using some reusable code helped to maintain order in my application and prevent duplication.

The job matching algorithm worked great after job requirements are added, as it generated the matching percentages and found the list of matched and missed skills. 

The other thing about ChatGPT, that worked good – was a debugging. With its help I received some information about database errors and ways to find the problem source.

5. What I changed and tested

After receiving the initial files for my application I installed and configured it on my Mac using Visual Studio Code, Python, Flask and MySQL.

While installing and configuring, I had a problem with MySQL, as it couldn't recognize some column called job_title.

Using MySQL Workbench I've found out, that my application was connected to an old database job_application_tracker, and it should be connected to job_tracker database.

I fixed duplicate DB_NAME entries in my .env configuration and restarted my Flask application to get rid of this error.

Then I've tested my application by creating records of companies, jobs, applications and contacts. I've checked if dashboard is displaying appropriate statistics and records are correctly associated via relationships in the database.

Also I've tested updates to application statuses, deletion of a temporary company record, using a job matching feature to calculate the matching percentage according to skill requirements.

I checked MySQL table definitions for my application to check if there are all necessary keys and JSON columns are there.

6. Conclusions

With the help of this project I gained some understanding of how full-stack web application connects its frontend, backend and database.

I got some practice in Flask routing and request handling as well as in connecting Flask application to MySQL and receiving/retrieving information.

I've also practiced using relational databases, foreign keys, JSON column.

One of the main things I've learned is about the importance of correct database configuration. Even if all your tables and SQL queries are good, your application may fail, as it was connecting to incorrect database.

Also it is clear, that AI-generated code still requires some debugging and functional tests, even when AI helps you to speed up the development process.