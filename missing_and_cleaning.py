import pandas as pd
import numpy as np

df = pd.read_csv("Online_Product_Reviews_missing.csv")

# ─────────────────────────────────────────────
# STEP 1: Fill missing values
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("FILLING MISSING VALUES...")
print("=" * 55)

# Rating — fill with mode (most common rating)
mode_rating = df["Rating"].mode()[0]
df["Rating"] = df["Rating"].fillna(mode_rating)
print(f"✔ Rating            → Filled with mode : {mode_rating}")

# Review Count — fill with median
median_rc = df["Review Count"].median()
df["Review Count"] = df["Review Count"].fillna(median_rc)
print(f"✔ Review Count      → Filled with median : {median_rc}")

# Helpful Votes — fill with median
median_hv = df["Helpful Votes"].median()
df["Helpful Votes"] = df["Helpful Votes"].fillna(median_hv)
print(f"✔ Helpful Votes     → Filled with median : {median_hv}")

# Total Votes — fill with median
median_tv = df["Total Votes"].median()
df["Total Votes"] = df["Total Votes"].fillna(median_tv)
print(f"✔ Total Votes       → Filled with median : {median_tv}")

# Helpfulness Score — fill with mean
mean_hs = round(df["Helpfulness Score"].mean(), 2)
df["Helpfulness Score"] = df["Helpfulness Score"].fillna(mean_hs)
print(f"✔ Helpfulness Score → Filled with mean  : {mean_hs}")

# Product Price — fill with mean
mean_pp = round(df["Product Price ($)"].mean(), 2)
df["Product Price ($)"] = df["Product Price ($)"].fillna(mean_pp)
print(f"✔ Product Price ($) → Filled with mean  : {mean_pp}")

# Delivery Days — fill with median
median_dd = df["Delivery Days"].median()
df["Delivery Days"] = df["Delivery Days"].fillna(median_dd)
print(f"✔ Delivery Days     → Filled with median : {median_dd}")

# Review Length — fill with median
median_rl = df["Review Length"].median()
df["Review Length"] = df["Review Length"].fillna(median_rl)
print(f"✔ Review Length     → Filled with median : {median_rl}")

# Sentiment Score — fill with mean
mean_ss = round(df["Sentiment Score"].mean(), 2)
df["Sentiment Score"] = df["Sentiment Score"].fillna(mean_ss)
print(f"✔ Sentiment Score   → Filled with mean  : {mean_ss}")

# ─────────────────────────────────────────────
# STEP 2: Verify
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("AFTER CLEANING — Missing Value Check")
print("=" * 55)
print(df.isnull().sum())
print(f"\nTotal Missing : {df.isnull().sum().sum()}")

df.to_csv("Online_Product_Reviews_cleaned.csv", index=False)
print("\n✅ Saved as 'Online_Product_Reviews_cleaned.csv'")
print("=" * 55)
