"""
CodSoft Data Analytics Internship
Task 3: Data Visualization Dashboard

Creates a set of customized charts (bar, line, pie, histogram, scatter)
using Matplotlib & Seaborn, and combines them into one dashboard image.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Build paths relative to this script's own location, so it runs correctly
# no matter what folder it's launched from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "data", "cleaned_sales_data.csv")
OUT_DIR = os.path.join(SCRIPT_DIR, "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")
PALETTE = "viridis"


def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["OrderDate"])
    df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)
    return df


def build_dashboard(df):
    fig, axes = plt.subplots(2, 3, figsize=(20, 11))
    fig.suptitle("Sales Data — Analytics Dashboard", fontsize=20, fontweight="bold")

    # 1. Bar chart: Revenue by category
    cat_rev = df.groupby("Category")["TotalAmount"].sum().sort_values(ascending=False)
    sns.barplot(x=cat_rev.values, y=cat_rev.index, hue=cat_rev.index,
                palette=PALETTE, legend=False, ax=axes[0, 0])
    axes[0, 0].set_title("Total Revenue by Category")
    axes[0, 0].set_xlabel("Revenue ($)")
    axes[0, 0].set_ylabel("Category")

    # 2. Line chart: Monthly revenue trend
    monthly_rev = df.groupby("Month")["TotalAmount"].sum()
    axes[0, 1].plot(monthly_rev.index, monthly_rev.values, marker="o", color="#2c7fb8")
    axes[0, 1].set_title("Monthly Revenue Trend")
    axes[0, 1].set_xlabel("Month")
    axes[0, 1].set_ylabel("Revenue ($)")
    axes[0, 1].tick_params(axis="x", rotation=75)

    # 3. Pie chart: Payment method share
    pay_counts = df["PaymentMethod"].value_counts()
    axes[0, 2].pie(pay_counts.values, labels=pay_counts.index, autopct="%1.1f%%",
                    colors=sns.color_palette(PALETTE, len(pay_counts)), startangle=90)
    axes[0, 2].set_title("Orders by Payment Method")

    # 4. Histogram: Order value distribution
    sns.histplot(df["TotalAmount"], bins=25, kde=True, color="#41b6c4", ax=axes[1, 0])
    axes[1, 0].set_title("Distribution of Order Values")
    axes[1, 0].set_xlabel("Order Value ($)")

    # 5. Scatter plot: UnitPrice vs Quantity, colored by category
    sns.scatterplot(data=df, x="UnitPrice", y="Quantity", hue="Category",
                     palette=PALETTE, alpha=0.7, ax=axes[1, 1], legend=False)
    axes[1, 1].set_title("Unit Price vs Quantity Purchased")
    axes[1, 1].set_xlabel("Unit Price ($)")
    axes[1, 1].set_ylabel("Quantity")

    # 6. Bar chart: Top 5 cities by revenue
    city_rev = df.groupby("City")["TotalAmount"].sum().sort_values(ascending=False).head(5)
    sns.barplot(x=city_rev.index, y=city_rev.values, hue=city_rev.index,
                palette="mako", legend=False, ax=axes[1, 2])
    axes[1, 2].set_title("Top 5 Cities by Revenue")
    axes[1, 2].set_xlabel("City")
    axes[1, 2].set_ylabel("Revenue ($)")
    axes[1, 2].tick_params(axis="x", rotation=30)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(f"{OUT_DIR}/dashboard_overview.png", dpi=150)
    plt.close()
    print(f"Saved combined dashboard to {OUT_DIR}/dashboard_overview.png")


def save_individual_charts(df):
    # Individual high-res charts, useful for reports/slides
    cat_rev = df.groupby("Category")["TotalAmount"].sum().sort_values(ascending=False)
    plt.figure(figsize=(9, 6))
    sns.barplot(x=cat_rev.values, y=cat_rev.index, hue=cat_rev.index, palette=PALETTE, legend=False)
    plt.title("Total Revenue by Category", fontsize=14, fontweight="bold")
    plt.xlabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/revenue_by_category.png", dpi=150)
    plt.close()

    monthly_rev = df.groupby("Month")["TotalAmount"].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_rev.index, monthly_rev.values, marker="o", color="#2c7fb8")
    plt.title("Monthly Revenue Trend", fontsize=14, fontweight="bold")
    plt.xticks(rotation=75)
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/monthly_revenue_trend.png", dpi=150)
    plt.close()

    print("Saved individual charts to outputs/")


if __name__ == "__main__":
    df = load_data()
    build_dashboard(df)
    save_individual_charts(df)
