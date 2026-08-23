# FIFA World Cup 2026 Analytics Dashboard

A portfolio-grade analytics application built to explore FIFA World Cup 2026 tournament, team, player, club, match, referee, and venue data through a modular data engineering and analytics pipeline.

**Live Dashboard:** https://worldcupanalysis-qstbcercnuzpg2kh5yfipx.streamlit.app/
**Repository:** `https://github.com/obeng-enoch/world_cup_analysis`

---

## Overview

This project transforms a relational FIFA World Cup dataset into an interactive analytical dashboard.

The project demonstrates an end-to-end workflow covering:

* Python
* pandas
* SQL
* SQLite
* ETL and data engineering
* Data cleaning and validation
* Modular Python architecture
* Streamlit
* Plotly
* Dashboard design
* Git and GitHub
* Reusable analytics and UI components

The objective is not simply to create a collection of charts. The project demonstrates how raw relational data can be transformed into a structured analytical database, exposed through a Python analytics layer, and presented as a reusable dashboard application.

---

## Dashboard

The application contains eight analytical pages:

| Page       | Focus                                                                  |
| ---------- | ---------------------------------------------------------------------- |
| Home       | Tournament overview and key headline metrics                           |
| Tournament | Tournament summary, standings, awards, and tournament-level analysis   |
| Matches    | Match results, scoring, match highlights, and match-level analysis     |
| Players    | Player performance, goals, assists, goalkeeper statistics, and leaders |
| Teams      | Team attacking and defensive performance                               |
| Clubs      | Club representation and player/team analysis                           |
| Referees   | Referee assignments and match-related statistics                       |
| Venues     | Venue usage and tournament venue analysis                              |

The dashboard is designed around reusable components, consistent styling, interactive Plotly visualizations, and a compact analytical experience rather than a long-form report.

---

## Architecture

The project follows a layered architecture with clear separation of responsibilities:

```text
Raw FIFA Dataset
       ↓
Python ETL Pipeline
       ↓
Cleaning & Validation
       ↓
SQLite Analytics Database
       ↓
SQL Analytics Layer
       ↓
Python Analytics API
       ↓
Dashboard Utility Layer
       ↓
Reusable UI / Chart Components
       ↓
Streamlit Dashboard Pages
```

### Project structure

```text
world_cup_analysis/
│
├── dashboard/
│   ├── app.py
│   ├── components/
│   ├── pages/
│   ├── theme/
│   └── utils/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── database/
│   └── world_cup_2026.db
│
├── docs/
│   ├── analytics_plan.md
│   ├── data_dictionary.md
│   └── dataset_inspection.md
│
├── sql/
│   ├── awards/
│   ├── club/
│   ├── events/
│   ├── match_analysis/
│   ├── players/
│   ├── referee/
│   ├── tactical/
│   ├── teams/
│   ├── tournament_overview/
│   └── venues/
│
├── src/
│   ├── analytics/
│   ├── build_database.py
│   ├── clean_data.py
│   ├── config.py
│   ├── update_database.py
│   └── validators.py
|
├── tests/
│   ├── analytics/
│   └── (unit tests for ETL, database, validators, and analytics layer)
|
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Data Pipeline

The project separates data ingestion, transformation, analytical querying, and presentation.

### ETL workflow

```text
Raw Dataset
    ↓
Load
    ↓
Clean
    ↓
Validate
    ↓
Build / Update SQLite Database
    ↓
Run Analytical SQL
    ↓
Expose Results Through Python
    ↓
Visualize in Streamlit
```

The ETL pipeline is responsible for:

* Loading raw FIFA data
* Cleaning and standardizing data
* Validating datasets
* Building/updating the SQLite database
* Loading cleaned data into the analytical database

The ETL process intentionally does **not** perform the Git pull for the raw dataset. Updating the raw repository remains a separate operation.

---

## Database

The canonical analytical database is:

```text
database/world_cup_2026.db
```

The validated database contains the major tournament entities and analytical datasets.

| Table                |  Rows |
| -------------------- | ----: |
| `tournament_stages`  |     7 |
| `venues`             |    16 |
| `referees`           |    28 |
| `teams`              |    48 |
| `squads_and_players` | 1,248 |
| `matches`            |   104 |
| `player_stats`       | 1,248 |
| `match_team_stats`   |   208 |
| `match_events`       |   834 |
| `match_lineups`      | 5,408 |

---

## SQL Analytics Layer

SQL is the project's analytical/business-logic layer.

The design follows the principle:

> **SQL owns the analytical/business logic. Queries are oganized by analytical domain, keeping database logic separate from Python and the dashboard presentation layer. **

Analytical calculations remain in SQL rather than being unnecessarily duplicated in Python.

The SQL layer covers areas including:

* Tournament overview
* Teams
* Players
* Clubs
* Matches
* Match events
* Tactical analysis
* Referees
* Venues
* Tournament awards

The Python analytics layer is intentionally lightweight. Its primary responsibilities are to:

1. Load SQL queries
2. Connect to SQLite
3. Execute queries
4. Return pandas DataFrames or scalar values

This separation keeps analytical logic independent from dashboard presentation.

---

## Python Analytics Layer

The `src/analytics/` package provides the interface between the SQL layer and the dashboard.

The analytics layer exposes reusable functions for the different analytical domains instead of embedding database queries directly inside Streamlit pages.

This allows the dashboard to remain focused on:

* Page composition
* Data presentation
* Visualization
* User interaction
* Reusable UI components

---

## Dashboard Design

The dashboard uses a reusable design system covering:

* Typography
* Icons
* Colors
* Metric cards
* Leader cards
* Award cards
* Chart components
* Page layouts
* Responsive styling

The application uses **Lucide-style icons rather than emoji-based UI elements** to maintain a consistent professional visual language.

Plotly is used for interactive analytical visualizations.

---

## Technology Stack

| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| Python     | Data processing and application logic |
| pandas     | Data transformation and analysis      |
| SQLite     | Analytical database                   |
| SQL        | Analytical/business logic             |
| Streamlit  | Dashboard application                 |
| Plotly     | Interactive visualization             |
| Git        | Version control                       |
| GitHub     | Source control and project hosting    |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/obeng-enoch/world_cup_analysis.git
cd world_cup_analysis
```

### 2. Create a virtual environment

Using Conda:

```bash
conda create -n world-cup-2026 python=3.12
conda activate world-cup-2026
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Dashboard Locally

From the project root:

```bash
python -m streamlit run dashboard/app.py
```

Using `python -m streamlit` is the verified launch method for the project because it explicitly runs Streamlit through the active Python environment.

---

## Updating the Database

If the raw FIFA dataset has been updated, first update the raw-data repository:

```bash
cd data/raw/worldcup
git pull
cd ../../..
```

Then rebuild/update the analytical database:

```bash
python -m src.update_database
```

Finally launch the dashboard:

```bash
python -m streamlit run dashboard/app.py
```

The Git pull is intentionally kept outside the ETL pipeline so that data retrieval and database transformation remain separate responsibilities.

---

## Validation

The project has been tested in a fresh Python environment to verify reproducibility.

The release validation included:

* Dependency installation
* pandas import
* Streamlit import
* Plotly import
* Analytics-layer imports
* Python compilation
* Streamlit startup
* Full dashboard navigation
* All eight dashboard pages

Compilation was verified with:

```bash
python -m compileall -q src dashboard
```

The dashboard was also successfully launched from the clean environment and all eight pages were verified.

## Testing

The project includes a pytest suite covering the ETL pipeline, database integrity, data validators, and the full Python analytics layer.

**152 tests passing.**

| Layer | Coverage |
| --- | --- |
| ETL / database build | Loader behavior, validation gating, table creation |
| Data cleaning | Cleaning functions across all raw datasets |
| Validators | Required columns, null checks, uniqueness, domain-specific rules |
| Analytics layer | Every analytics module (tournament, teams, players, matches, clubs, awards, events, referees, tactical, venues) |

Run the full suite with:

\`\`\`bash
pytest
\`\`\`

---

## Development Principles

The project follows several engineering principles:

### Separation of concerns

Each layer has a defined responsibility.

### SQL owns analytical logic

Business and analytical calculations remain in SQL.

### Reusable components

Common dashboard elements are implemented as reusable components rather than duplicated across pages.

### YAGNI

The project avoids unnecessary abstractions and complexity.

### Incremental validation

Major changes are tested before moving to the next layer.

### Portfolio-quality engineering

The objective is to demonstrate not only analytical ability, but also the ability to structure, validate, document, and deploy a complete data application.

---

## Project Status

**Status: Deployed and live**

The core ETL pipeline, analytical database, SQL layer, Python analytics layer, dashboard architecture, visual system, and all 8 dashboard pages (Home plus 7 domain pages)  are complete and tested.

The project has passed clean-environment validation, a 152 automated suite, and is live on Streamlit Cloud.

---

## Author

**Enoch Obeng Mensah**

Data Analytics | Data Engineering | Python | SQL | Streamlit

GitHub: `https://github.com/obeng-enoch`