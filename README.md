---
date: 2024-04-10T11:33:24.888352
author: AutoGPT <info@agpt.co>
---

# test

Based on the provided user feedback, the task involves creating an API that echoes back any text it receives. This requirement signifies the need for a simple yet functional API endpoint that accepts text input from the user and returns the same text as the output. Utilizing the specified tech stack, which includes Python as the programming language, FastAPI for the API framework, PostgreSQL for the database, and Prisma as the Object Relational Mapping (ORM) tool, the implementation will focus on setting up a RESTful API Service. The FastAPI framework will be utilized to set up the API routes, taking advantage of its asynchronous request handling and its automatic interactive API documentation. Since the core functionality is to echo back received text, the use of PostgreSQL and Prisma might only come into play if there's a need to store the requests or responses for logging or monitoring purposes. To summarize, the API will be a straightforward implementation focusing primarily on request handling and response mechanism to fulfill the echo functionality desired.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'test'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
