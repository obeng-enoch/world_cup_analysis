# FIFA World Cup 2026 Analytics Plan

## Purpose

This document defines the analytics roadmap for the FIFA World Cup 2026 Analytics Dashboard.

The objective is to transform the cleaned FIFA World Cup dataset into meaningful football insights through SQL analytics and present those insights through an interactive Streamlit dashboard.

The dashboard is designed to support both:

- Live tournament tracking during the competition
- Complete tournament retrospective analysis after the final match

The final dashboard should answer questions about:

- Tournament performance
- Team success
- Player achievements
- Club contributions
- Match patterns
- Tactical trends
- Tournament awards
- Historical records

---

# Analytics Development Workflow

Each analytical feature should follow the same workflow:

1. Define the football question.
2. Identify required database tables.
3. Write SQL query.
4. Test query against SQLite database.
5. Validate results.
6. Save query in appropriate SQL file.
7. Connect results to Streamlit dashboard.

---

# Analytics Architecture

```
SQLite Database

        |

SQL Analytics Layer

        |

Python Analytics Interface

        |

Streamlit Dashboard
```

Responsibilities:

## SQL Layer

Responsible for:

- joins
- aggregations
- ranking
- filtering
- calculations
- football business logic

## Python Analytics Layer

Responsible for:

- executing SQL queries
- returning pandas DataFrames
- preparing data for visualization

## Streamlit Layer

Responsible for:

- dashboard layout
- user interaction
- filters
- charts
- tables
- presentation

---

# SQL Analytics Structure

```
sql/

├── tournament_overview.sql
├── team_analysis.sql
├── player_analysis.sql
├── club_analysis.sql
├── match_analysis.sql
├── venue_analysis.sql
├── referee_analysis.sql
├── tactical_analysis.sql
├── event_analysis.sql
└── awards_records.sql
```

---

# 1. Tournament Overview

## SQL File

`tournament_overview.sql`

## Purpose

Provide a complete overview of the FIFA World Cup tournament.

This will power the dashboard homepage.

---

## Data Sources

Tables:

- matches
- teams
- venues
- players
- match_events
- match_team_stats

---

# Tournament KPIs

## Tournament Status

- Tournament Champion
- Runner-up
- Third Place
- Fourth Place

## Tournament Statistics

- Total Teams
- Total Players
- Total Clubs Represented
- Total Venues
- Total Matches
- Completed Matches
- Upcoming Matches
- Total Goals
- Average Goals Per Match
- Total Yellow Cards
- Total Red Cards
- Total Attendance (if available)
- Average Attendance (if available)

---

# Tournament Analysis

Questions:

- How many matches were played?
- Which stage produced the most goals?
- Which stage had the most competitive matches?
- How many goals were scored in each round?
- How did scoring change throughout the tournament?

---

# Dashboard Components

- KPI Cards
- Tournament Summary
- Stage Performance Charts
- Match Progress Timeline


---

# 2. Team Analysis

## SQL File

`team_analysis.sql`

## Purpose

Analyse national team performance.

---

## Data Sources

Tables:

- teams
- matches
- match_team_stats
- match_events

---

# KPIs

- Highest Scoring Team
- Best Defensive Team
- Most Wins
- Highest xG Team
- Highest Possession Team
- Best Pass Accuracy

---

# Analysis

## Attacking

- Goals Scored
- Shots
- Shots on Target
- Expected Goals
- Conversion Rate

## Defensive

- Goals Conceded
- Clean Sheets
- Tackles
- Interceptions

## General Performance

- Wins
- Draws
- Losses
- Goal Difference
- Points

## Discipline

- Yellow Cards
- Red Cards

---

# Dashboard Components

- Team Rankings
- Team Comparison Charts
- Performance Tables


---

# 3. Player Analysis

## SQL File

`player_analysis.sql`

## Purpose

Evaluate individual player performances.

---

## Data Sources

Tables:

- squads_and_players
- player_stats
- match_events
- match_lineups

---

# KPIs

- Top Scorer
- Top Assist Provider
- Most Minutes Played
- Most Valuable Player (if available)
- Most Player of Match Awards (if available)

---

# Analysis

## Attacking

- Goals
- Assists
- Goal Contributions
- Shots
- Shots on Target
- xG

## Playing Time

- Appearances
- Starts
- Minutes Played

## Defensive

- Tackles
- Interceptions
- Clearances

## Discipline

- Yellow Cards
- Red Cards

## Goalkeepers

- Saves
- Clean Sheets
- Save Percentage


---

# Dashboard Components

- Player Leaderboards
- Top Performer Charts
- Player Comparison Tables


---

# 4. Club Analysis

## SQL File

`club_analysis.sql`

## Purpose

Analyse how professional clubs contributed to the FIFA World Cup through their players.

This section connects international football performance with club football.

---

## Data Sources

Tables:

- squads_and_players
- player_stats
- matches
- teams

---

# KPIs

- Total Clubs Represented
- Club With Most Players
- Highest Scoring Club
- Most Assists By Club
- Most Minutes Played
- Club With Most Champions

---

# Representation Analysis

Questions:

- Which clubs supplied the most players?
- Which clubs represented the most national teams?
- Which leagues contributed the most players?

Metrics:

- Players per club
- Countries represented
- Leagues represented


---

# Attacking Performance

Metrics:

- Goals by Club
- Assists by Club
- Goal Contributions
- Goals per Player
- Goals per 90 Minutes


---

# Playing Time Analysis

Metrics:

- Total Minutes
- Total Appearances
- Total Starts
- Average Minutes


---

# Tournament Success

Metrics:

- Clubs with Champions
- Clubs with Finalists
- Clubs with Semi-finalists
- Clubs with Quarter-finalists


---

# Discipline Analysis

Metrics:

- Yellow Cards
- Red Cards


---

# Dashboard Components

- Club Rankings
- Club Contribution Charts
- Club Performance Tables


---

# 5. Match Analysis

## SQL File

`match_analysis.sql`

## Purpose

Analyse individual matches.

---

## Data Sources

Tables:

- matches
- match_team_stats
- match_events


---

# Analysis

- Highest Scoring Matches
- Biggest Victories
- Closest Matches
- Highest xG Matches
- Most Competitive Games
- Penalty Shootouts
- Most Cards
- Most Shots


---

# Dashboard Components

- Match Tables
- Match Comparison Charts


---

# 6. Venue Analysis

## SQL File

`venue_analysis.sql`

## Purpose

Analyse stadium performance.

---

## Data Sources

Tables:

- venues
- matches


---

# Analysis

- Matches Hosted
- Goals per Venue
- Average Goals
- Attendance
- Highest Attendance
- Stadium Activity


---

# 7. Referee Analysis

## SQL File

`referee_analysis.sql`

## Purpose

Analyse officiating patterns.

---

## Data Sources

Tables:

- referees
- matches
- match_events


---

# Analysis

- Matches Officiated
- Yellow Cards
- Red Cards
- Penalties
- Fouls
- Average Cards Per Match


---

# 8. Tactical Analysis

## SQL File

`tactical_analysis.sql`

## Purpose

Understand tactical trends.

---

## Data Sources

Tables:

- match_team_stats
- teams
- matches


---

# Analysis

- Possession vs Winning
- Passing Accuracy vs Winning
- xG vs Goals
- Shot Conversion
- Defensive Efficiency
- Attacking Efficiency


---

# Dashboard Components

- Scatter Plots
- Correlation Charts
- Tactical Comparison


---

# 9. Event Analysis

## SQL File

`event_analysis.sql`

## Purpose

Analyse match events.

---

## Data Sources

Tables:

- match_events
- matches


---

# Analysis

- Goals by Minute
- Goals by Half
- Stoppage Time Goals
- Card Timing
- Substitution Timing
- First Goal Impact
- Equalisers


---

# 10. Awards and Tournament Records

## SQL File

`awards_records.sql`

## Purpose

Capture official tournament achievements and memorable records.

---

## Data Sources

Tables:

- player_stats
- matches
- teams
- tournament_awards (if created)

---

# FIFA Awards

Track:

## Golden Ball

Best Player

## Silver Ball

Second Best Player

## Bronze Ball

Third Best Player

## Golden Boot

Top Goalscorer

## Silver Boot

Second Highest Goalscorer

## Bronze Boot

Third Highest Goalscorer

## Golden Glove

Best Goalkeeper

## Best Young Player

## Fair Play Award


---

# Tournament Records

Analyse:

- Highest scoring match
- Biggest winning margin
- Fastest goal
- Latest goal
- Most goals by player
- Most assists
- Most cards in a match
- Most penalties
- Longest penalty shootout


---

# Tournament Story Insights

Generate automated insights such as:

- Champion team performance summary
- Top scoring team
- Best defensive team
- Best performing clubs
- Most influential players
- Tournament records achieved


---

# Final Dashboard Pages

The Streamlit dashboard will contain:

1. Home / Tournament Overview
2. Teams
3. Players
4. Clubs
5. Matches
6. Venues
7. Referees
8. Tactical Analysis
9. Events
10. Awards & Records


---

# Development Checklist

For each analytics category:

- [ ] Define football questions
- [ ] Identify tables
- [ ] Write SQL queries
- [ ] Test queries
- [ ] Validate results
- [ ] Connect to Python analytics layer
- [ ] Add dashboard visualizations


---

# Expected Final Deliverables

At completion, the project will contain:

- Production-style SQL analytics layer
- Modular Python analytics interface
- Interactive Streamlit dashboard
- Tournament summary
- Team analysis
- Player analysis
- Club contribution analysis
- Awards and records analysis
- Complete project documentation

The final result will demonstrate an end-to-end football analytics workflow:

Raw FIFA Data

↓

Python ETL Pipeline

↓

SQLite Database

↓

SQL Analytics Layer

↓

Python Analytics Interface

↓

Streamlit Dashboard

↓

Professional Portfolio Project