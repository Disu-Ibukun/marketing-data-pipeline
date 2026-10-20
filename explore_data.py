
import pandas as pd

ads = pd.read_csv(
    "new_ads_de_randomized.csv",
    dtype={"ad_id": "string"}
)

stats = pd.read_csv(
    "ads_stats.csv",
    dtype={"ad_id": "string"}
)

# Examine the first five records.
print(ads.head())
print(stats.head())

# Examine dataset size.
print("Ads:", ads.shape)
print("Statistics:", stats.shape)

# Examine missing values.
print(stats.isna().sum())


#Examine unique rows
print(ads.nunique())


# Check whether each ad/date combination is unique.
print(
    "Repeated ad/date combinations:",
    stats.duplicated(subset=["ad_id", "ad_date"]).sum()
)

# Check missing values.
print("\nMissing values:")
print(stats.isna().sum())

# Check whether statistics reference ads that don't exist.
print(
    "\nUnmatched ad references:",
    (~stats["ad_id"].isin(ads["ad_id"])).sum()
)
