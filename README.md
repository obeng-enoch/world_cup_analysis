# FIFA World Cup 2026 Analysis

## Project Overview

This project analyzes FIFA World Cup 2026 player and club performance using a relational SQLite dataset. The goal is to identify top-performing players, national teams, and domestic clubs based on goals, assists, and total goal contributions.

The project combines SQL for querying a normalized database, Python for analysis, and Streamlit for an interactive dashboard.

## Dataset

The dataset contains information about:

- Teams
- Players
- Matches
- Match events
- Player statistics
- Venues
- Referees
- Team match statistics

Source: FIFA World Cup 2026 dataset from Kaggle, GitHub, and Hugging Face.

## Tools Used

- Python
- Pandas
- SQLite
- Matplotlib
- Seaborn
- Plotly
- Streamlit

## Project Structure

```text
world_cup_analysis/
├── data/
│   └── raw/
│       └── worldcup/
│           ├── fifa_world_cup_2026.db
│           ├── player_stats.csv
│           ├── squads_and_players.csv
│           ├── teams.csv
│           └── other raw dataset files
├── dashboard/
│   └── app.py
├── notebooks/
│   └── club_rival_analysis.ipynb
└── README.md
```

## Key Questions

This project focuses on answering the following questions:

- Which players have the most goals and assists?
- Which domestic clubs have contributed the most goals through their players?
- Which clubs have the highest total goal contributions?
- Which national teams are producing the strongest attacking output?
- How can tournament data be presented clearly in an interactive dashboard?

## Analysis Summary

The notebook explores player and club performance by connecting to the SQLite database and querying the relevant tables. The main analysis joins `player_stats` with `squads_and_players` to connect each player's World Cup performance with their domestic club.

The key metric used is total goal contributions:

```text
total goal contributions = goals + assists
```

This gives a broader view of attacking impact than goals alone.

## Current Findings

- Real Madrid C. F. leads the club ranking by total goal contributions.
- Paris Saint-Germain and Bayern Munich are also among the strongest contributors.
- Some major clubs, such as Barcelona and Chelsea, are not currently among the top clubs by total goal contributions in this dataset.
- Goal contributions provide a better view of attacking influence than goals alone because assists are also included.

## Dashboard

The Streamlit dashboard provides an interactive way to explore the data. It currently includes:

- Key tournament metrics
- Top goal scorers
- Top clubs by goals contributed
- Team-level goal and assist comparison
- Sidebar filtering by team

Run the dashboard with:

```bash
streamlit run dashboard/app.py
```

## How To Run The Project

1. Clone or download the project.
2. Make sure the dataset is available in `data/raw/worldcup/`.
3. Install the required Python packages.
4. Open the notebook or run the Streamlit dashboard.

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit
```

Run the notebook:

```bash
jupyter notebook notebooks/club_rival_analysis.ipynb
```

Run the dashboard:

```bash
streamlit run dashboard/app.py
```

## Important Data Note

Some numeric columns in the SQLite database are stored as text. For accurate calculations, numeric fields such as `goals`, `assists`, and `minutes_played` should be converted to numbers in Python or cast in SQL.

Example SQL cast:

```sql
SUM(CAST(goals AS INTEGER)) AS total_goals
```

Example pandas conversion:

```python
player_stats["goals"] = pd.to_numeric(player_stats["goals"], errors="coerce")
```

## Future Improvements

Planned improvements include:

- Fixing numeric type conversion throughout the notebook and dashboard
- Adding more player-level comparison charts
- Adding goals-per-90 and assists-per-90 metrics
- Improving dashboard filters for club, team, and position
- Adding a `requirements.txt` file
- Adding screenshots of the dashboard
- Expanding the conclusion section with stronger football insights

## Conclusion

This project demonstrates how SQL, Python, and Streamlit can be used together to analyze football tournament data. It is still being improved, but the foundation is in place for a strong sports analytics portfolio project.
