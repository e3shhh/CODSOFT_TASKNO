# Task 3 — Data Visualization Dashboard

## Objective
Turn the cleaned dataset into a set of clear, customized visualizations.

## What the script does (`visualization_dashboard.py`)
Builds a 6-panel dashboard (`outputs/dashboard_overview.png`) combining:
- **Bar chart** — total revenue by category
- **Line chart** — monthly revenue trend
- **Pie chart** — order share by payment method
- **Histogram** — distribution of order values
- **Scatter plot** — unit price vs. quantity purchased, colored by category
- **Bar chart** — top 5 cities by revenue

All charts are customized with titles, axis labels, and consistent color
palettes. Individual high-resolution versions of the key charts are also
saved separately for use in reports or slides.

## Run it
```bash
python visualization_dashboard.py
```

## Files
- `data/cleaned_sales_data.csv` — cleaned dataset from Task 1
- `outputs/dashboard_overview.png` — combined 6-panel dashboard
- `outputs/revenue_by_category.png`, `outputs/monthly_revenue_trend.png` — standalone charts

## Bonus (not included here)
An interactive Power BI / Tableau version can be built on top of
`cleaned_sales_data.csv` for a fully interactive dashboard.
