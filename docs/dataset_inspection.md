# Dataset Inspection

This document records the inspection findings for every dataset before any
cleaning or validation logic is implemented.

Following the YAGNI principle, cleaning code is only written when the inspection
reveals an actual problem.

---


## teams.csv

Rows: 48

Columns: 8

### Cleaning Required

- ✓ Load CSV
- ✗ Remove duplicates
- ✗ Handle missing values
- ✗ Convert dates
- ✗ Rename columns
- ✗ Change data types

### Validation Required

- ✓ DataFrame not empty
- ✓ Required columns exist
- ✓ team_id unique
- ✓ Required columns not null
- ✓ fifa_code unique
- ✓ Positive rankings
- ✓ Positive Elo ratings

## venues.csv

Rows: 16

Columns: 8

### Cleaning Required

- ✓ Load CSV
- ✓ Convert date columns
- ✗ Remove duplicates
- ✗ Rename columns
- ✗ Handle missing values

### Validation Required

- ✓ DataFrame not empty
- ✓ Required columns exist
- ✓ player_id unique
- ✓ Required columns not null

## player_stats.csv

Rows: 1248

Columns: 21

### Cleaning Required

- ✓ Load CSV
- ✓ Convert date columns
- ✗ Remove duplicates
- ✗ Rename columns
- ✗ Handle missing values

### Validation Required

- ✓ DataFrame not empty
- ✓ Required columns exist
- ✓ player_id unique
- ✓ Required columns not null

---

## matches

### Overview

- Rows: 104
- Columns: 17
- Duplicate rows: 0
- Primary key: `match_id`

### Column Summary

| Column | Observation |
|--------|-------------|
| match_id | Unique, no missing values |
| date | Stored as string; should be converted to datetime |
| kickoff_time_utc | Stored as string |
| stage_id | Complete |
| venue_id | Complete |
| home_team_id | 2 missing values |
| away_team_id | 2 missing values |
| home_score | 4 missing values |
| away_score | 4 missing values |
| home_penalty_score | Present only for penalty shootouts |
| away_penalty_score | Present only for penalty shootouts |
| status | Complete |
| result_type | 4 missing values |
| home_xg | 4 missing values |
| away_xg | 4 missing values |
| referee_id | Complete |
| player_of_the_match_id | 4 missing values |

### Data Quality Findings

- No duplicate rows.
- `match_id` appears to be a reliable primary key.
- Missing values in score-related columns appear to correspond to matches that have not yet been played.
- Penalty score columns are intentionally sparse and should not be treated as missing data errors.
- Only the `date` column requires transformation during cleaning.

### Cleaning Decisions

- Convert `date` to datetime.
- Preserve legitimate missing values.
- No additional transformations required at this stage.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- `match_id` is unique.
- Required columns contain no null values.

Do not require values for:

- Scores
- Penalty scores
- xG
- Result type
- Player of the Match

These fields are legitimately null for future fixtures.