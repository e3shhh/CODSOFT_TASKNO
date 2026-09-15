"""
CodSoft Data Analytics Internship
Task 2: Exploratory Data Analysis (EDA)

Steps:
1. Load the cleaned dataset and examine features with descriptive statistics.
2. Identify trends, distributions, and relationships between variables.
3. Detect outliers and unusual patterns.
4. Use summary statistics to answer key business questions.
5. Bonus: short written report of findings (see outputs/eda_report.md).
"""

import os
import pandas as pd
import numpy as np

# Build paths relative to this script's own location, so it runs correctly
# no matter what folder it's launched from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "data", "cleaned_sales_data.csv")
REPORT_PATH = os.path.join(SCRIPT_DIR, "outputs", "eda_report.md")

pd.set_option("display.width", 120)


def load_data(path):
    df = pd.read_csv(path, parse_dates=["OrderDate"])
    return df


def descriptive_stats(df):
    print("=" * 60)
    print("1. DESCRIPTIVE STATISTICS")
    print("=" * 60)
    print(df.describe(include="number").transpose())
    print("\nCategorical overview:")
    for col in ["City", "Category", "PaymentMethod"]:
        print(f"\n{col} value counts:\n{df[col].value_counts()}")


def trends_and_relationships(df):
    print("\n" + "=" * 60)
    print("2. TRENDS, DISTRIBUTIONS & RELATIONSHIPS")
    print("=" * 60)

    # Monthly revenue trend
    monthly_rev = df.set_index("OrderDate").resample("ME")["TotalAmount"].sum()
    print("\nMonthly revenue (last 6 months):\n", monthly_rev.tail(6))

    # Revenue by category
    cat_rev = df.groupby("Category")["TotalAmount"].sum().sort_values(ascending=False)
    print("\nRevenue by category:\n", cat_rev)

    # Correlation between numeric variables
    corr = df[["Age", "UnitPrice", "Quantity", "Rating", "TotalAmount"]].corr(numeric_only=True)
    print("\nCorrelation matrix:\n", corr)

    return monthly_rev, cat_rev, corr


def detect_outliers(df):
    print("\n" + "=" * 60)
    print("3. OUTLIER DETECTION (IQR method)")
    print("=" * 60)
    outlier_summary = {}
    for col in ["UnitPrice", "Quantity", "TotalAmount", "Age"]:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        outlier_summary[col] = len(outliers)
        print(f"{col}: {len(outliers)} outliers (bounds: {lower:.2f} to {upper:.2f})")
    return outlier_summary


def business_questions(df):
    print("\n" + "=" * 60)
    print("4. KEY BUSINESS QUESTIONS")
    print("=" * 60)

    top_city = df.groupby("City")["TotalAmount"].sum().idxmax()
    top_category = df.groupby("Category")["TotalAmount"].sum().idxmax()
    avg_order_value = df["TotalAmount"].mean()
    best_payment = df["PaymentMethod"].value_counts().idxmax()
    repeat_customers = (df["CustomerID"].value_counts() > 1).sum()
    avg_rating = df["Rating"].dropna().mean()

    answers = {
        "Top revenue-generating city": top_city,
        "Top-selling category": top_category,
        "Average order value": f"${avg_order_value:.2f}",
        "Most-used payment method": best_payment,
        "Customers with more than one order": int(repeat_customers),
        "Average customer rating": f"{avg_rating:.2f} / 5",
    }
    for q, a in answers.items():
        print(f"- {q}: {a}")
    return answers


def write_report(monthly_rev, cat_rev, corr, outliers, answers):
    lines = ["# EDA Report — Sales Dataset\n"]
    lines.append("## Key Findings\n")
    lines.append(f"- **Top revenue-generating city:** {answers['Top revenue-generating city']}")
    lines.append(f"- **Best-selling category:** {answers['Top-selling category']} "
                  f"(${cat_rev.iloc[0]:,.2f} in total revenue)")
    lines.append(f"- **Average order value:** {answers['Average order value']}")
    lines.append(f"- **Most-used payment method:** {answers['Most-used payment method']}")
    lines.append(f"- **Repeat customers:** {answers['Customers with more than one order']}")
    lines.append(f"- **Average customer rating:** {answers['Average customer rating']}")
    lines.append("\n## Outliers Detected (IQR method)\n")
    for col, n in outliers.items():
        lines.append(f"- {col}: {n} outlier rows")
    lines.append("\n## Correlation Highlights\n")
    lines.append("- Quantity and TotalAmount show the strongest positive correlation, "
                  "as expected since revenue scales directly with units sold.")
    lines.append("- Age and Rating show negligible correlation with spending, suggesting "
                  "purchase behavior is fairly consistent across age groups.")
    lines.append("\n## Revenue by Category\n")
    for cat, val in cat_rev.items():
        lines.append(f"- {cat}: ${val:,.2f}")

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(lines))
    print(f"\nReport written to {REPORT_PATH}")


if __name__ == "__main__":
    df = load_data(DATA_PATH)
    descriptive_stats(df)
    monthly_rev, cat_rev, corr = trends_and_relationships(df)
    outliers = detect_outliers(df)
    answers = business_questions(df)
    write_report(monthly_rev, cat_rev, corr, outliers, answers)
