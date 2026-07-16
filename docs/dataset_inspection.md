# Dataset Inspection

This document records the exploratory data analysis performed on each dataset before implementing the ETL pipeline.

The purpose of this inspection is to:

- Understand the structure and quality of each dataset.
- Identify any cleaning requirements before loading the data.
- Define validation rules based on actual data characteristics.
- Document engineering decisions made during ETL development.

Following the YAGNI (You Aren't Gonna Need It) principle, cleaning and validation logic are implemented only when supported by evidence from the inspection rather than assumptions.

---


## teams.csv

### Overview

- Rows: 48
- Columns: 8
- Duplicate rows: 0
- Primary key: `team_id`

### Column Summary

| Column | Observation |
|---------|-------------|
| team_id | Unique, no missing values |
| team_name | Complete, unique team names |
| fifa_code | Complete, unique FIFA codes |
| group_letter | Complete |
| confederation | Complete |
| fifa_ranking_pre_tournament | Complete, positive integer values |
| elo_rating | Complete, positive integer values |
| manager_name | Complete |

### Data Quality Findings

- No missing values.
- No duplicate rows.
- Data types are appropriate for all columns.
- `team_id` appears to be a reliable primary key.
- `fifa_code` values are unique and suitable as alternate identifiers.
- FIFA rankings and Elo ratings are positive numeric values.

### Cleaning Decisions

- Load the dataset.
- Preserve existing data types.
- No transformations required.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- `team_id` is unique.
- `fifa_code` is unique.
- Required columns contain no null values.
- `fifa_ranking_pre_tournament` contains positive values.
- `elo_rating` contains positive values.

Do not require validation for:

- `manager_name` beyond ensuring it is present, as names may legitimately vary in format.

## venues.csv

### Overview

- Rows: 16
- Columns: 8
- Duplicate rows: 0
- Primary key: `venue_id`

### Column Summary

| Column | Observation |
|---------|-------------|
| venue_id | Unique, no missing values |
| stadium_name | Complete |
| city | Complete |
| country | Complete |
| capacity | Complete, positive integer values |
| latitude | Complete, valid numeric values |
| longitude | Complete, valid numeric values |
| elevation_meters | Complete, numeric values |

### Data Quality Findings

- No missing values.
- No duplicate rows.
- Data types are appropriate for all columns.
- `venue_id` appears to be a reliable primary key.
- Geographic coordinates are stored as floating-point values.
- Stadium capacities are positive integers.
- Elevation values are present for every venue.

### Cleaning Decisions

- Load the dataset.
- Preserve existing data types.
- No transformations required.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- `venue_id` is unique.
- Required columns contain no null values.
- `capacity` contains positive values.
- `latitude` values fall within the valid range (-90 to 90).
- `longitude` values fall within the valid range (-180 to 180).
- `elevation_meters` contains numeric values.

Do not require validation for:

- Stadium names, cities, or countries beyond ensuring they are present, as these are descriptive text fields.

## tournament_stages.csv

### Overview

- Rows: 7
- Columns: 3
- Duplicate rows: 0
- Primary key: `stage_id`

### Column Summary

| Column | Observation |
|---------|-------------|
| stage_id | Unique, no missing values |
| stage_name | Complete |
| is_knockout | Boolean values only |

### Data Quality Findings

- No missing values.
- No duplicate rows.
- Data types are already appropriate.
- Dataset requires no structural cleaning.

### Cleaning Decisions

- Load the dataset.
- Preserve existing data types.
- No transformations required.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- `stage_id` is unique.
- Required columns contain no null values.
- `is_knockout` contains boolean values.

## referees.csv

### Overview

- Rows: 28
- Columns: 4
- Duplicate rows: 0
- Primary key: `referee_id`

### Column Summary

| Column | Observation |
|---------|-------------|
| referee_id | Unique, no missing values |
| name | Complete |
| country | Complete |
| avg_cards_per_game | Complete, positive numeric values |

### Data Quality Findings

- No missing values.
- No duplicate rows.
- Data types are appropriate for all columns.
- `referee_id` appears to be a reliable primary key.
- `avg_cards_per_game` contains positive numeric values representing each referee's historical average number of cards issued per match.

### Cleaning Decisions

- Load the dataset.
- Preserve existing data types.
- No transformations required.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- `referee_id` is unique.
- Required columns contain no null values.
- `avg_cards_per_game` contains non-negative numeric values.

Do not require validation for:

- `name`
- `country`

Beyond ensuring they are present, these descriptive text fields do not require additional validation.

## player_stats.csv

### Overview

- Rows: 1248
- Columns: 21
- Duplicate rows: 0
- Primary key: `player_id`

### Column Summary

| Column | Observation |
|---------|-------------|
| player_id | Unique, no missing values |
| player_name | Complete; duplicate names exist, so names are not unique identifiers |
| team_id | Complete |
| position | Complete |
| matches_played | Complete |
| matches_started | Complete |
| minutes_played | Complete |
| goals | Complete |
| assists | Complete |
| shots | Entire column is currently missing |
| shots_on_target | Entire column is currently missing |
| yellow_cards | Complete |
| red_cards | Complete |
| penalty_goals | Complete |
| own_goals | Complete |
| clean_sheets | Available only for goalkeepers |
| saves | Available only for goalkeepers |
| goals_conceded | Available only for goalkeepers |
| average_rating | Entire column is currently missing |
| data_source | Missing for some records |
| last_verified | Complete; stored as string and should be converted to datetime |

### Data Quality Findings

- No duplicate rows.
- `player_id` appears to be a reliable primary key.
- Several statistical fields (`shots`, `shots_on_target`, and `average_rating`) are completely empty and should be preserved as missing rather than treated as errors.
- Goalkeeper-specific statistics (`clean_sheets`, `saves`, and `goals_conceded`) are intentionally null for outfield players.
- `data_source` contains missing values but is metadata rather than analytical data.
- `last_verified` should be converted from string to datetime during cleaning.

### Cleaning Decisions

- Convert `last_verified` to datetime.
- Preserve legitimate missing values.
- Do not remove or impute missing statistical columns.
- No additional transformations required.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- `player_id` is unique.
- Required columns contain no null values, excluding fields with legitimate missing values.
- Numeric statistical columns contain non-negative values.
- `last_verified` is successfully converted to datetime.

Do not require values for:

- `shots`
- `shots_on_target`
- `average_rating`
- `clean_sheets`
- `saves`
- `goals_conceded`
- `data_source`

These fields are legitimately incomplete based on the available source data or player position.

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