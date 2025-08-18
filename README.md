# Contact.app

Learning HTMX by working through [Hypermedia Systems](https://hypermedia.systems/).

## Stack

- Python
- Flask
- Jinja2

## Setup

1. Create and activate a virtual environment (recommended):
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `py -m venv .venv; .\.venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install -r requirements.txt`

## Running the app

Option A: Using Python directly
- `python main.py`

Option B: Using Flask's CLI
- macOS/Linux:
  - `export FLASK_APP=main.py`
  - `flask run`
- Windows (PowerShell):
  - `$env:FLASK_APP = "main.py"`
  - `flask run`

Then open http://127.0.0.1:5000/ in your browser. You should see "Hello World!".

## Notes
- The development server in `main.py` runs with `debug=True` for convenience. Do not use this in production; use a WSGI server instead (e.g., gunicorn or waitress).
