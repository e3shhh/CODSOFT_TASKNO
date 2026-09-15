"""
CodSoft Data Analytics Internship
Task 1: Data Cleaning & Preprocessing

Steps:
1. Import the dataset and inspect its structure.
2. Identify missing values, duplicate records, and inconsistent entries.
3. Clean the dataset: handle nulls, remove duplicates, fix data types & text.
4. Save the cleaned dataset as a new CSV (bonus).
"""

import os
import pandas as pd
import numpy as np

# Build paths relative to this script's own location, so it runs correctly
# no matter what folder VS Code (or any terminal) launches it from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = os.path.join(SCRIPT_DIR, "data", "raw_sales_data.csv")
CLEAN_PATH = os.path.join(SCRIPT_DIR, "outputs", "cleaned_sales_data.csv")


def load_and_inspect(path):
    df = pd.read_csv(path)
    print("=" * 60)
    print("STEP 1: INSPECT RAW DATA")
    print("=" * 60)
    print(f"Shape: {df.shape}")
    print("\nColumn dtypes:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())
    print("\nMissing values per column:\n", df.isnull().sum())
    print(f"\nExact duplicate rows: {df.duplicated().sum()}")
    return df


def clean_data(df):
    print("\n" + "=" * 60)
    print("STEP 2: CLEAN THE DATA")
    print("=" * 60)

    df = df.copy()

    # --- Remove exact duplicate rows ---
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} exact duplicate rows.")

    # --- Standardize text columns (strip whitespace, fix casing) ---
    df["City"] = df["City"].astype(str).str.strip().str.title()
    df["City"] = df["City"].replace("Nan", np.nan)

    df["PaymentMethod"] = df["PaymentMethod"].astype(str).str.strip().str.title()

    df["CustomerName"] = df["CustomerName"].astype(str).str.strip()
    df["CustomerName"] = df["CustomerName"].replace("Nan", np.nan)

    # --- Fix inconsistent date formats (mixed YYYY-MM-DD and DD/MM/YYYY) ---
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], format="mixed", dayfirst=False, errors="coerce")

    # --- Fix invalid Quantity (negative values are data-entry errors) ---
    invalid_qty = (df["Quantity"] <= 0).sum()
    print(f"Invalid (non-positive) Quantity values found: {invalid_qty}")
    df = df[df["Quantity"] > 0]

    # --- Handle missing values ---
    # Numeric: fill Age with median, Rating left as-is (genuinely "no rating given")
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Age"] = df["Age"].astype(int)

    # Categorical: fill missing City/CustomerName with 'Unknown'
    df["City"] = df["City"].fillna("Unknown")
    df["CustomerName"] = df["CustomerName"].fillna("Unknown")

    # Drop rows where OrderDate could not be parsed (unusable for analysis)
    before = len(df)
    df = df.dropna(subset=["OrderDate"])
    print(f"Dropped {before - len(df)} rows with unparseable OrderDate.")

    # --- Correct data types ---
    df["UnitPrice"] = df["UnitPrice"].astype(float).round(2)
    df["Quantity"] = df["Quantity"].astype(int)
    df["Rating"] = df["Rating"].astype("Int64")  # nullable integer, keeps NaN for "no rating"

    # --- Feature engineering: total order value ---
    df["TotalAmount"] = (df["UnitPrice"] * df["Quantity"]).round(2)

    # --- Final duplicate check on key business columns ---
    before = len(df)
    df = df.drop_duplicates(subset=["OrderID"])
    print(f"Removed {before - len(df)} duplicate OrderIDs.")

    df = df.reset_index(drop=True)
    return df


def summarize(df):
    print("\n" + "=" * 60)
    print("STEP 3: CLEANED DATA SUMMARY")
    print("=" * 60)
    print(f"Final shape: {df.shape}")
    print("\nMissing values per column after cleaning:\n", df.isnull().sum())
    print("\nDtypes after cleaning:\n", df.dtypes)
    print("\nDescriptive stats:\n", df.describe(include="all").transpose())


if __name__ == "__main__":
    raw_df = load_and_inspect(RAW_PATH)
    clean_df = clean_data(raw_df)
    summarize(clean_df)

    os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)
    clean_df.to_csv(CLEAN_PATH, index=False)
    print(f"\nCleaned dataset saved to: {CLEAN_PATH}")
