# Dataset Inspection

This document records the inspection findings for every dataset before any
cleaning or validation logic is implemented.

Following the YAGNI principle, cleaning code is only written when the inspection
reveals an actual problem.

---

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