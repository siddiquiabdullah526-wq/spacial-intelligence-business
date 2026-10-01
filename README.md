# Spatial Intelligence for Business

Faculty Led Research Project (Sept 2026 - April 2027).
Combines GIS with large language models (Claude API) to turn spatial data into
clear, actionable business recommendations. Southern California is the testbed.

## Pipeline

```
Stage 1: Spatial Data Layer  ->  Stage 2: SI Engine  ->  Stage 3: LLM Interpretation  ->  Stage 4: Business Decision
(Census, OSM, Google Places,     (SI-1 / SI-2 / SI-3      (Claude API via LangChain)        (Question, Key Finding, Map,
 Esri Living Atlas)               analysis modules)                                           Recommendation, Confidence)
```

## Team and ownership

| Folder | Track | Question | Owner |
|---|---|---|---|
| `/si1` | Location Intelligence | Where should we open our next location? | Stella |
| `/si2` | Market Gap Intelligence | Which markets are we underserving? | Sushma |
| `/si3` | Territory Intelligence | How should we structure service or delivery zones? | Glira |
| `/shared_pipeline` | Integration and LLM Engineer | Shared pipeline + Claude API | Abdullah |
| `/docs` | BI and Evaluation Lead | Report template, evaluation | Arezou |
| `/data` | Local data (gitignored) | Never committed | Everyone |

Faculty lead: Dr. Mehrdad Koohikamali

## Quick start

```bash
git clone <repo-url>
cd spatial-intelligence-business
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then add your own keys
python shared_pipeline/test_claude.py
```

## Rules

- Never commit `.env`, API keys, or anything in `/data`.
- Work on a branch per track (`si1-...`, `si2-...`, `si3-...`) and open a pull request.
- Each SI module returns results in the standard format in `docs/pipeline_spec.md`.
