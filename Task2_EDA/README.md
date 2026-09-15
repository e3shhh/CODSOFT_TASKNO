# Task 2 — Exploratory Data Analysis (EDA)

## Objective
Explore the cleaned sales dataset to surface trends, relationships,
outliers, and answers to key business questions.

## What the script does (`eda_analysis.py`)
1. **Descriptive statistics** for numeric and categorical columns.
2. **Trends & relationships**: monthly revenue trend, revenue by
   category, and a correlation matrix across numeric variables.
3. **Outlier detection** using the IQR method on `UnitPrice`,
   `Quantity`, `TotalAmount`, and `Age`.
4. **Business questions answered**, e.g.:
   - Which city generates the most revenue?
   - What's the best-selling category?
   - What's the average order value?
   - Which payment method is most used?
   - How many repeat customers are there?
5. **Bonus**: writes a short markdown findings report to
   `outputs/eda_report.md`.

## Run it
```bash
python eda_analysis.py
```

## Files
- `data/cleaned_sales_data.csv` — cleaned dataset from Task 1
- `outputs/eda_report.md` — written summary of key findings
