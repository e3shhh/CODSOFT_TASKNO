# Task 1 — Data Cleaning & Preprocessing

## Objective
Import a raw sales dataset, inspect its structure, identify data quality
issues, and produce an analysis-ready cleaned dataset.

## What the script does (`data_cleaning.py`)
1. **Loads & inspects** `data/raw_sales_data.csv` — shape, dtypes, missing
   values, and duplicate rows.
2. **Identifies issues**: missing `Age`/`City`/`CustomerName`, exact
   duplicate rows, negative `Quantity` values (data-entry errors), and
   inconsistent date formats (`YYYY-MM-DD` mixed with `DD/MM/YYYY`).
3. **Cleans the data**:
   - Removes exact duplicate rows and duplicate `OrderID`s
   - Standardizes text (trims whitespace, fixes inconsistent casing like
     `"mumbai"` / `"MUMBAI"` → `"Mumbai"`)
   - Parses mixed date formats into a single consistent `datetime` type
   - Removes invalid (non-positive) `Quantity` rows
   - Fills missing `Age` with the median, missing `City`/`CustomerName`
     with `"Unknown"`
   - Fixes column data types (float, int, nullable int for ratings)
   - Adds a derived `TotalAmount` column (`UnitPrice × Quantity`)
4. **Saves the cleaned dataset** to `outputs/cleaned_sales_data.csv` (bonus ✅).

## Run it
```bash
python data_cleaning.py
```

## Files
- `data/raw_sales_data.csv` — raw, intentionally messy input data
- `outputs/cleaned_sales_data.csv` — cleaned output (used by Tasks 2–4)
