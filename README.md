# CODSOFT_TASKSNO — Data Analytics Internship

This repository contains my completed tasks for the **CodSoft Data Analytics
Internship**. Per the internship guidelines, a minimum of **3 tasks** is
required for successful completion — this submission covers Tasks 1–3,
which together form a complete data pipeline: clean the raw data, explore
it, then visualize the findings.

| Task | Folder | Description |
|------|--------|-------------|
| 1 | [`Task1_Data_Cleaning`](./Task1_Data_Cleaning) | Data cleaning & preprocessing with Pandas |
| 2 | [`Task2_EDA`](./Task2_EDA) | Exploratory Data Analysis (EDA) |
| 3 | [`Task3_Data_Visualization`](./Task3_Data_Visualization) | Visualization dashboard (Matplotlib/Seaborn) |

## How the tasks connect
1. **Task 1** takes a raw, messy sales dataset and produces a cleaned
   `cleaned_sales_data.csv`.
2. **Task 2** loads that cleaned dataset to run exploratory analysis —
   stats, trends, correlations, outliers, and business Q&A.
3. **Task 3** uses the same cleaned dataset to build a 6-panel
   visualization dashboard summarizing the key findings.

## Tech Stack
- Python 3
- Pandas, NumPy
- Matplotlib, Seaborn

## How to Run
Each task folder is self-contained. From inside a task folder:

```bash
pip install -r ../requirements.txt
python <script_name>.py
```

Outputs (cleaned CSVs, charts, reports) are written to that task's
`outputs/` folder.

## Submission Notes
- GitHub repo name: `CODSOFT_TASKSNO` (as required by the instructions)
- A demo video walking through the project will be posted on LinkedIn
  with `#codsoft #internship #dataanalytics`, tagging CodSoft, along with
  this repo's link.

## About the Internship
Completed as part of the CodSoft Data Analytics Virtual Internship.
🔗 [codsoft.in](https://www.codsoft.in)
