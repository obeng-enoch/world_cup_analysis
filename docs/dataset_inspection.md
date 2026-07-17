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

## squads_and_players.csv

### Overview

- Rows: 1248
- Columns: 10
- Duplicate rows: 0
- Primary key: `player_id`

### Column Summary

| Column | Observation |
|---------|-------------|
| player_id | Unique, no missing values |
| team_id | Complete |
| player_name | Complete |
| position | Complete |
| club_team | Complete |
| market_value_eur | Complete, stored as integer values |
| caps | Complete, stored as integer values |
| date_of_birth | Complete; currently stored as string and should be converted to datetime |
| height_cm | Complete, stored as integer values |
| goals | Complete, stored as integer values |

### Data Quality Findings

- No missing values.
- No duplicate rows.
- Data types are appropriate for all columns except `date_of_birth`, which is stored as a string.
- `player_id` appears to be a reliable primary key.
- Numeric player attributes (`market_value_eur`, `caps`, `height_cm`, and `goals`) are complete and contain no missing values.
- No structural cleaning issues were identified during inspection.

### Cleaning Decisions

- Convert `date_of_birth` from string to datetime.
- Preserve all remaining values and data types.
- No additional transformations required.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- `player_id` is unique.
- Required columns contain no null values.
- `market_value_eur` contains non-negative values.
- `caps` contains non-negative values.
- `height_cm` contains positive values.
- `goals` contains non-negative values.
- `date_of_birth` is successfully converted to datetime.

Do not require validation for:

- `player_name`
- `position`
- `club_team`

Beyond ensuring they are present, these descriptive text fields do not require additional validation.

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

## match_team_stats.csv

### Overview

- Rows: 200
- Columns: 12
- Duplicate rows: 0
- Primary key: Composite (`match_id`, `team_id`)

### Column Summary

| Column | Observation |
|---------|-------------|
| match_id | Complete |
| team_id | Complete |
| possession_pct | Complete |
| total_shots | Complete |
| shots_on_target | Complete |
| corners | Complete |
| fouls | Complete |
| offsides | Complete |
| saves | Complete |
| player_of_the_match | Present for 100 rows; legitimately missing for the corresponding opposing team |
| data_source | Complete |
| last_updated | Complete; stored as string and should be converted to datetime |

### Data Quality Findings

- No duplicate rows.
- No missing values except for `player_of_the_match`.
- The combination of `match_id` and `team_id` appears to uniquely identify each record.
- `player_of_the_match` contains 100 missing values, which appear to be intentional because only one Player of the Match award is recorded per match.
- `last_updated` is stored as a string and should be converted to datetime during cleaning.

### Cleaning Decisions

- Convert `last_updated` from string to datetime.
- Preserve legitimate missing values in `player_of_the_match`.
- No additional transformations required.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- Required columns contain no null values except `player_of_the_match`.
- The combination of `match_id` and `team_id` is unique.
- `possession_pct` contains values between 0 and 100.
- `total_shots` contains non-negative values.
- `shots_on_target` contains non-negative values.
- `corners` contains non-negative values.
- `fouls` contains non-negative values.
- `offsides` contains non-negative values.
- `saves` contains non-negative values.
- `last_updated` is successfully converted to datetime.

Do not require values for:

- `player_of_the_match`

This field is legitimately missing for one team in each match because only a single Player of the Match award is assigned.

## match_events.csv

### Overview

* Rows: 790
* Columns: 6
* Duplicate rows: 0
* Primary key: `event_id`

### Column Summary

| Column     | Observation                                                                            |
| ---------- | -------------------------------------------------------------------------------------- |
| event_id   | Complete; unique identifier for each match event                                       |
| match_id   | Complete; references the corresponding match                                           |
| minute     | Complete; stored as string to preserve football minute notation (e.g., `45+2`, `90+5`) |
| event_type | Complete; categorical field describing the type of match event                         |
| team_id    | Complete; references the team associated with the event                                |
| player_id  | Complete; references the player involved in the event                                  |

### Data Quality Findings

* No duplicate rows.
* No missing values were found in any column.
* `event_id` appears to uniquely identify each record.
* `minute` is stored as a string rather than a numeric data type. This is intentional because football event times may include stoppage-time notation (e.g., `45+2`, `90+5`), which should not be converted to integers.
* `event_type` is a categorical field containing different types of match events (e.g., Goal, Yellow Card, Red Card, VAR Review).
* Multiple events may occur in the same match, involve the same player, or occur in the same minute. These are expected characteristics of football match event data and do not represent data quality issues.

### Cleaning Decisions

* Preserve the `minute` column as a string.
* No datetime conversion is required.
* No missing values require handling.
* No duplicate rows require removal.
* No additional transformations are required.

### Validation Decisions

Validate:

* DataFrame is not empty.
* Required columns exist.
* Required columns contain no null values.
* `event_id` is unique.
* `minute` is stored as a string/object data type.
* `event_type` contains no missing values.
* `match_id` contains valid values.
* `team_id` contains valid values.
* `player_id` contains valid values.

Do not allow missing values for any column.

## match_lineups.csv

### Overview

- Rows: 5200
- Columns: 7
- Duplicate rows: 0
- Primary key: `lineup_id`

### Column Summary

| Column | Observation |
|---------|-------------|
| lineup_id | Complete; unique identifier for each lineup record |
| match_id | Complete; references the corresponding match |
| player_id | Complete; references the player included in the lineup |
| team_id | Complete; references the team associated with the player |
| is_starting_xi | Complete; binary indicator showing whether the player started the match |
| tactical_position | Complete; categorical field describing the player's tactical position |
| minutes_played | Complete; numeric field representing the number of minutes played by the player |

### Data Quality Findings

- No duplicate rows.
- No missing values were found in any column.
- `lineup_id` appears to uniquely identify each lineup record.
- `match_id`, `player_id`, and `team_id` contain complete values and can be used to establish relationships with other tables.
- `is_starting_xi` is stored as an integer field and represents a binary value indicating whether a player was part of the starting XI.
- `tactical_position` is stored as a string field containing player positions such as goalkeeper, defender, and other tactical roles.
- `minutes_played` contains values ranging from 0 to 120, which is expected because matches can include extra time.
- Multiple records per match are expected because each match contains multiple players across both teams.

### Cleaning Decisions

- Preserve the `is_starting_xi` column as an integer because it represents a binary indicator.
- Preserve the `tactical_position` column as text because it contains categorical position information.
- No missing values require handling.
- No duplicate rows require removal.
- No additional transformations are currently required.

### Validation Decisions

Validate:

- DataFrame is not empty.
- Required columns exist.
- Required columns contain no null values.
- `lineup_id` is unique.
- `is_starting_xi` contains only valid binary values (0 or 1).
- `minutes_played` contains non-negative values.
- `minutes_played` does not exceed 120 minutes.
- `tactical_position` contains no missing values.

No columns are expected to contain legitimate missing values.