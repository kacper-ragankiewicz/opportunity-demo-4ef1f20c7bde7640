# Full-stack proof of approach

This repository is a small technical demonstration for a role that combines **Python backend work** with a **responsive frontend**.

It demonstrates one focused capability:
- a Flask API with validated filtering and clear JSON responses
- a lightweight frontend that fetches that API and renders a responsive dashboard

## Included
- `GET /api/work-items` with optional `status` filter
- validation for unsupported filters with a JSON error response
- responsive UI with summary cards, filter control, loading state, empty state, and error state
- focused tests covering API success and failure cases

## Intentionally simplified
- in-memory fixture data instead of a database
- no auth, background jobs, or deployment setup
- no client-specific business logic

## Run
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

## Test
```bash
python -m unittest tests.py
```

## Verification status
This environment does not allow execution, so the repository includes runnable code and tests but makes no runtime-verification claim here.


## Verification status

Static validation of paths, sizes and Python/JSON syntax only. Application, tests and build NOT executed by the generator.
