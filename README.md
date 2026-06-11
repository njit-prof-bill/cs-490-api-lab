# CS 490 API Lab: The Bridge of Death

In this lab, you will implement a small REST API using Python and FastAPI. Each team will be assigned one question and one correct answer. Your job is to implement two REST endpoints:

```http
GET /your-team-name/question
POST /your-team-name/answer
```

The goal is not to build a large application. The goal is to practice implementing a simple API contract.

## What You Will Learn

By completing this lab, you will practice:

- Forking a GitHub repository
- Cloning your fork locally
- Creating a branch
- Running a Python FastAPI server
- Implementing REST endpoints
- Testing endpoints with `curl`
- Submitting a pull request back to the original repository

## Repository

Start from this repository:

```text
https://github.com/njit-prof-bill/cs-490-api-lab
```

## Step 1: Fork the Repository

Open the repository in your browser:

```text
https://github.com/njit-prof-bill/cs-490-api-lab
```

Click the **Fork** button in the upper-right corner of the page.

GitHub will create a copy of the repository under your own GitHub account.

Your fork will have a URL similar to:

```text
https://github.com/YOUR-GITHUB-USERNAME/cs-490-api-lab
```

## Step 2: Clone Your Fork

On your forked repository page, click the green **Code** button and copy the repository URL.

Then clone your fork to your computer:

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/cs-490-api-lab.git
```

Move into the project directory:

```bash
cd cs-490-api-lab
```

## Step 3: Create a Branch

Create a new branch for your team’s work.

Use your team name in the branch name.

Example:

```bash
git checkout -b breeze-api
```

Another example:

```bash
git checkout -b merge-survivors-api
```

Do not work directly on the `main` branch.

## Step 4: Create and Activate a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, your terminal prompt should show `(.venv)`.

## Step 5: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Step 6: Run the Server Locally

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

If the server starts correctly, you should see output showing that the application is running locally.

Open this URL in your browser:

```text
http://127.0.0.1:8000
```

You can also open the automatically generated API documentation:

```text
http://127.0.0.1:8000/docs
```

## Step 7: Test the Instructor Endpoint

Before editing your team file, verify that the application works.

Run this command:

```bash
curl http://127.0.0.1:8000/instructor/question
```

You should receive a JSON response similar to:

```json
{
  "question": "What have the Romans ever done for us?"
}
```

Now test the answer endpoint:

```bash
curl -X POST http://127.0.0.1:8000/instructor/answer \
  -H "Content-Type: application/json" \
  -d '{"answer": "The aqueducts?"}'
```

You should receive a JSON response similar to:

```json
{
  "correct": true,
  "message": "You may pass."
}
```

If this works, your local environment is ready.

## Step 8: Find Your Team File

Each team has its own Python file in the `teams` directory.

Find the file assigned to your team.

Examples:

```text
teams/breeze.py
teams/claude_scholars.py
teams/merge_survivors.py
teams/team_dragons.py
teams/team101.py
teams/the_shrimps.py
```

Only edit your team’s file.

Do not edit another team’s file.

Do not edit `main.py` unless instructed.

Do not edit the test files.

## Step 9: Implement Your GET Endpoint

Your team file contains a stub similar to this:

```python
@router.get("/question")
def get_question():
    pass
```

Replace the `pass` statement with code that returns your assigned question.

The response must follow this exact JSON shape:

```json
{
  "question": "Your assigned question goes here"
}
```

Example:

```python
@router.get("/question")
def get_question():
    return {
        "question": "What is your name?"
    }
```

The field name must be exactly:

```text
question
```

Do not rename it to `questionText`, `prompt`, `myQuestion`, or anything else.

The contract matters.

## Step 10: Implement Your POST Endpoint

Your team file also contains a stub similar to this:

```python
@router.post("/answer")
def post_answer(request: AnswerRequest):
    pass
```

Replace the `pass` statement with code that checks the submitted answer.

The request body will look like this:

```json
{
  "answer": "Some answer"
}
```

Your response must follow this exact JSON shape:

```json
{
  "correct": true,
  "message": "You may pass."
}
```

or:

```json
{
  "correct": false,
  "message": "Into the Gorge of Eternal Peril!"
}
```

Example implementation:

```python
ANSWER = "Arthur, King of the Britons"

@router.post("/answer")
def post_answer(request: AnswerRequest):
    correct = request.answer.strip().lower() == ANSWER.strip().lower()

    return {
        "correct": correct,
        "message": "You may pass." if correct else "Into the Gorge of Eternal Peril!",
    }
```

The field names must be exactly:

```text
correct
message
```

Do not change them.

## Step 11: Test Your Team Endpoint

Restart the server if necessary:

```bash
uvicorn main:app --reload
```

Test your question endpoint.

Example:

```bash
curl http://127.0.0.1:8000/breeze/question
```

Replace `breeze` with your team’s route.

Test your answer endpoint.

Example:

```bash
curl -X POST http://127.0.0.1:8000/breeze/answer \
  -H "Content-Type: application/json" \
  -d '{"answer": "Arthur, King of the Britons"}'
```

Also test an incorrect answer:

```bash
curl -X POST http://127.0.0.1:8000/breeze/answer \
  -H "Content-Type: application/json" \
  -d '{"answer": "wrong answer"}'
```

Your endpoint should return `correct: true` for the correct answer and `correct: false` for an incorrect answer.

## Step 12: Run the Basic Tests

Run the test suite:

```bash
python -m pytest
```

The tests are intentionally limited. They verify that the shared application and instructor endpoint work.

You are responsible for manually testing your own team endpoint with `curl`.

## Step 13: Check Your Git Status

Before committing, check which files changed:

```bash
git status
```

You should only see your team file changed.

If you changed files that you were not supposed to edit, stop and ask for help.

## Step 14: Commit Your Changes

Add your team file:

```bash
git add teams/YOUR_TEAM_FILE.py
```

Example:

```bash
git add teams/breeze.py
```

Commit your work:

```bash
git commit -m "Implement Breeze bridge API"
```

Use your actual team name in the commit message.

## Step 15: Push Your Branch

Push your branch to your fork:

```bash
git push origin YOUR-BRANCH-NAME
```

Example:

```bash
git push origin breeze-api
```

## Step 16: Open a Pull Request

Go to your fork on GitHub.

GitHub should show a button asking if you want to open a pull request.

Open a pull request back to:

```text
njit-prof-bill/cs-490-api-lab
```

Make sure the pull request is going from your branch into the original repository.

Use a clear pull request title.

Example:

```text
Implement Breeze API endpoints
```

In the pull request description, include:

```text
Team name:
Assigned question:
Assigned answer:
How we tested:
```

Example:

```text
Team name: Breeze
Assigned question: What is your name?
Assigned answer: Arthur, King of the Britons
How we tested: We ran the server locally and tested both endpoints using curl.
```

## API Contract

Every team must implement the same contract.

### Get Question

```http
GET /team-route/question
```

Response:

```json
{
  "question": "Question text"
}
```

### Submit Answer

```http
POST /team-route/answer
```

Request:

```json
{
  "answer": "Answer text"
}
```

Response:

```json
{
  "correct": true,
  "message": "You may pass."
}
```

or:

```json
{
  "correct": false,
  "message": "Into the Gorge of Eternal Peril!"
}
```

## Important Rules

Only edit your team file.

Do not edit `main.py`.

Do not edit another team’s file.

Do not edit the tests.

Do not change the API contract.

Do not rename the JSON fields.

Do not change the route names.

Your API must return valid JSON.
