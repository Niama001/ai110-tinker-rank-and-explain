# StudySync (AI110 Tinker Starter)

Starter code for the AI110 **Tinker 1B / 2B / 3B** in-class activities. All three tinkers
build on this one project, each working in a different module.

| Tinker | Focus | Files you'll work in |
|---|---|---|
| 1B, Split the Logic | Writing your first `pytest` test, then a cross-file refactor | `scoring.py`, `scoring_helpers.py`, `test_scoring.py` |
| 2B, Wire It Up | Streamlit `session_state`, input validation, dataclasses, recurring dates | `sessions.py`, `app.py` |
| 3B, Rank & Explain | CSV loading, weighted scoring that returns reasons, ranking, a data-flow diagram | `ranking.py`, `data/study_spots.csv`, `diagram.mmd` |

## My Rank & Explain work (Tinker 3B)

The **Find a Study Spot** tab loads campus study spots from a CSV, scores each one against a student profile, ranks the whole collection, and explains each result.

- `load_study_spots()` reads `data/study_spots.csv` with `csv.DictReader` and converts `distance_miles` to float and `seats_available` to int.
- `score_study_spot()` awards points for noise, distance, and seats, and returns a score plus a list of reasons.
- `rank_study_spots()` scores every spot, sorts with `sorted(..., reverse=True)`, and keeps the top k.
- `format_results()` prints one explained line per result.
- `reflection.md` covers how my weighting could create a filter bubble.
- `diagram.mmd` is a Mermaid flowchart of the pipeline: CSV, scoring, ranking, formatted output.

Run it:

```bash
python ranking.py
python -m streamlit run app.py
```

## Setup

Fork this repo, then clone **your fork**:

```bash
git clone https://github.com/<YOUR-GITHUB-USERNAME>/ai110-tinker-studysync-starter.git
cd ai110-tinker-studysync-starter
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
```

macOS, Linux, Git Bash or WSL:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies and run:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```

Run the tests:

```bash
pytest
```

## Files

- `app.py` — Streamlit entry point, wires the three tabs together
- `scoring.py` — `session_rating()` and the Session Scorer tab
- `scoring_helpers.py` — helpers extracted during Tinker 1B
- `sessions.py` — session log, the Tinker 2B surface
- `ranking.py` — study-spot ranking, the Tinker 3B surface
- `data/study_spots.csv` — sample data for ranking
- `diagram.mmd` — Mermaid data-flow diagram, completed in Tinker 3B
- `reflection.md` — written reflection on bias in the scoring weights
- `test_scoring.py` — starting point for your own tests

Your instructor will tell you which tinker you're on. Follow the activity on the course portal.