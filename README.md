# FIFA World Cup 2026 Analytics Dashboard

An end-to-end data project analyzing the completed FIFA World Cup 2026 — built as a portfolio-grade analytics product rather than a static report. The project follows a strict layered architecture: a Python ETL pipeline loads raw tournament data into SQLite, a SQL analytics layer owns all football-analytics logic, a Python analytics API exposes that data cleanly, and a Streamlit dashboard with a custom design system presents it.

## Project Philosophy

**Analytics before visualization.** Every metric on the dashboard has to answer a real football question before it earns a place in the UI.

The project is organized in layers, and no layer is allowed to duplicate another's responsibility:

```
Raw FIFA Dataset
      ↓
Python ETL Pipeline            (import, clean, validate, load — no dashboard logic)
      ↓
SQLite Database                (database/world_cup_2026.db — single source of truth)
      ↓
SQL Analytics Layer            (owns all football analytics logic; one file = one query)
      ↓
Python Analytics API           (loads + executes SQL, returns scalars/DataFrames only)
      ↓
Dashboard Utilities            (combines analytics calls into page-ready datasets)
      ↓
Dashboard Theme System         (single source of truth for colors, type, spacing, icons)
      ↓
Reusable Components            (presentation only — cards, charts, tables)
      ↓
Dashboard Pages                (layout only — no SQL, no business logic)
```

## Tools Used

Python · SQLite · SQL · Pandas · Streamlit · Plotly

## Dataset

Sourced from a FIFA World Cup 2026 dataset (Kaggle / GitHub / Hugging Face), covering:

- Teams, players, squads and clubs
- Matches and match events
- Player statistics and match-team statistics
- Venues and referees
- Tournament awards (Golden/Silver/Bronze Ball & Boot, Golden Glove, Best Young Player, Fair Play Award)

Since the tournament has concluded, this is a **completed-tournament analysis dashboard**, not a live tracker.

## Project Structure

```
world_cup_analysis/
├── database/
│   └── world_cup_2026.db          # canonical SQLite database
├── sql/                            # SQL analytics layer — one file per query
│   ├── tournament_overview/
│   ├── players/
│   ├── teams/
│   ├── awards/
│   ├── club/
│   ├── match_analysis/
│   ├── events/
│   ├── referee/
│   └── tactical/
├── src/
│   └── analytics/                  # Python analytics API
│       ├── database.py
│       ├── query_loader.py
│       ├── tournament.py
│       ├── players.py
│       ├── teams.py
│       ├── matches.py
│       ├── clubs.py
│       ├── venues.py
│       ├── referees.py
│       ├── events.py
│       ├── awards.py
│       └── tactical.py
├── dashboard/
│   ├── app.py                      # home page
│   ├── config.py
│   ├── pages/
│   │   └── 1_Tournament.py         # + remaining pages in progress
│   ├── components/                 # reusable UI (metric, podium, award cards, charts)
│   ├── theme/                      # design system: colors, typography, spacing, icons, css
│   ├── utils/                      # page-ready data preparation
│   └── assets/
│       └── icons/                  # local Lucide SVG icon set
├── notebooks/                      # early exploratory analysis (see note below)
└── README.md
```

## Key Questions This Project Answers

- Which players and teams produced the strongest attacking output?
- Which domestic clubs contributed the most through their players at the tournament?
- How did each team's tournament run end (champion, runner-up, stage eliminated)?
- Who won each individual award, and how did the tournament's goals and outcomes break down by stage?
- How can completed tournament data be presented clearly as an interactive analytics product?

## Current Findings

- **Champion: Spain** · **Runner-up: Argentina** · **Third place: England**
- Tournament totals: 48 teams, 1,248 players, 104 matches, 308 goals
- Full award winners (Golden/Silver/Bronze Ball, Golden/Silver/Bronze Boot, Golden Glove, Best Young Player, Fair Play) are tracked in a dedicated awards table and surfaced on the Tournament page

## Dashboard

The Streamlit dashboard is built as a proper design system, not a one-off script:

- A **theme package** (`dashboard/theme/`) centralizes every color, font, spacing value, and icon — no component hardcodes styling
- A **local Lucide SVG icon set** replaces emoji icons for a more polished look
- Reusable **card components** (KPI metric cards, podium/standings cards, award cards) and a **Plotly chart library** with a consistent visual style across every chart
- Currently live: home page with tournament-wide KPIs, and a Tournament Overview page (summary KPIs, final standings, goals-by-stage chart, full standings table, tournament awards)
- In progress: Players, Teams, Matches, Clubs, Venues, Referees, Events, and Awards pages, each following the same architecture

Run it with:
```bash
PYTHONPATH=. streamlit run dashboard/app.py
```

## How To Run The Project

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Confirm `database/world_cup_2026.db` is present (or run the ETL pipeline to build it — see below).
4. Launch the dashboard:
   ```bash
   PYTHONPATH=. streamlit run dashboard/app.py
   ```

To rebuild the database from raw data:
```bash
git pull
python -m src.update_database
```

## A Note on the `notebooks/` Folder

This project began as an exploratory notebook-based analysis before being rebuilt with a proper ETL → SQL → Analytics API → Dashboard architecture. The early notebook(s) are kept for historical reference but no longer reflect how the project actually works — all analytics logic now lives in the `sql/` and `src/analytics/` layers described above.

## Roadmap

- [ ] Finish remaining dashboard pages (Players, Teams, Matches, Clubs, Venues, Referees, Events, Awards)
- [ ] Add remaining Tournament page visualizations (Match Outcomes, Goals by Team)
- [ ] Plotly chart library v2 (richer theming, responsive sizing, consistent legends)
- [ ] Layout helper module for reusable page grids
- [ ] Mobile responsiveness pass
- [ ] Automated tests
- [ ] Final polish: loading/empty states, tooltips, accessibility, number formatting
- [ ] Portfolio screenshots and demo video

## Conclusion

This project demonstrates a full, disciplined data pipeline — from raw tournament data through SQL analytics and a Python API to a themed, component-driven Streamlit dashboard — built as a portfolio-quality sports analytics product rather than a single analysis script.