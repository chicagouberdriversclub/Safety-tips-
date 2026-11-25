# Project Overview

Safety-tips- is the Chicago Uber driver safety repo for the Uber Senior Driving Club and the Chicago 0ver25drivers Club.

## What is in this repo

- `safety.txt` — the plain-text safety tips for Chicago Uber drivers.
- `README.md` — the same safety tips, in Markdown.
- `src/app.py` — a small starter app (`greet()`).
- `tests/test_app.py` — tests for the starter app.
- `docs/overview.md` — this file.
- `.github/workflows/ci.yml` — GitHub Actions CI, runs pytest on push/PR to main.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
cp .env.example .env
```

## Run App and Tests

```bash
PYTHONPATH=src python src/app.py
PYTHONPATH=src pytest
```

## Contact

Email chicago.uberdrivers@gmail.com
