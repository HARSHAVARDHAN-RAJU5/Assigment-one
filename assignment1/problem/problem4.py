# import pandas as pd

# df = pd.read_csv("new_clean.csv")
# df["date"] = pd.to_datetime(df["date"])

# df["year"] = df["date"].dt.year
# df["month"] = df["date"].dt.month
# df["day"] = df["date"].dt.day

# df["is_pongal"] = (
#     (df["month"] == 1) &
#     (df["day"] >= 5) &
#     (df["day"] <= 20)
# )

# df["is_baseline"] = (
#     (df["month"] == 1) &
#     ((df["day"] <= 4) | (df["day"] >= 21))
# )

# pongal = (
#     df[df["is_pongal"]]
#     .groupby(["sku", "item_name", "year"], as_index=False)
#     .agg(pongal_qty=("qty", "sum"),
#          pongal_days=("date", "nunique"))
# )

# baseline = (
#     df[df["is_baseline"]]
#     .groupby(["sku", "item_name", "year"], as_index=False)
#     .agg(baseline_qty=("qty", "sum"),
#          baseline_days=("date", "nunique"))
# )

# merged = pongal.merge(
#     baseline,
#     on=["sku", "item_name", "year"],
#     how="left"
# )

# merged["baseline_avg_per_day"] = merged["baseline_qty"] / merged["baseline_days"]
# merged["baseline_15day_qty"] = merged["baseline_avg_per_day"] * 15
# merged["uplift"] = merged["pongal_qty"] / merged["baseline_15day_qty"]

# spikes = merged[merged["uplift"] >= 2].copy()

# spikes = spikes.sort_values("uplift", ascending=False)

# spikes.to_csv("pongal.csv", index=False)

# print("pongal.csv created with spike SKUs only.")


# import pandas as pd

# df = pd.read_csv("pongal.csv")

# # count spike years per SKU
# year_count = (
#     df.groupby(["sku", "item_name"])["year"]
#       .nunique()
#       .reset_index(name="spike_years")
# )

# # keep only SKUs that spiked in all 4 years
# consistent = year_count[year_count["spike_years"] == 1]

# # merge back to get uplift values
# merged = df.merge(
#     consistent[["sku", "item_name"]],
#     on=["sku", "item_name"],
#     how="inner"
# )

# # summarize
# final = (
#     merged.groupby(["sku", "item_name"], as_index=False)
#           .agg(
#               avg_spike_uplift=("uplift", "mean"),
#               min_uplift=("uplift", "min"),
#               max_uplift=("uplift", "max")
#           )
# )

# final = final.sort_values("avg_spike_uplift", ascending=False)

# final.to_csv("pongal_c.csv", index=False)

# print("pongal_consistent.csv created")


import pandas as pd

df = pd.read_csv("new_clean.csv")
df["date"] = pd.to_datetime(df["date"])

df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

df["is_pongal"] = (
    (df["month"] == 1) &
    (df["day"] >= 5) &
    (df["day"] <= 20)
)

df["is_baseline"] = (
    (df["month"] == 1) &
    ((df["day"] <= 4) | (df["day"] >= 21))
)

pongal = (
    df[df["is_pongal"]]
    .groupby(["sku", "item_name"], as_index=False)
    .agg(
        pongal_qty=("qty", "sum"),
        pongal_days=("date", "nunique")
    )
)

baseline = (
    df[df["is_baseline"]]
    .groupby(["sku", "item_name"], as_index=False)
    .agg(
        baseline_qty=("qty", "sum"),
        baseline_days=("date", "nunique")
    )
)

merged = pongal.merge(
    baseline,
    on=["sku", "item_name"],
    how="inner"
)

merged["baseline_avg_per_day"] = (
    merged["baseline_qty"] / merged["baseline_days"]
)

merged["baseline_15day_qty"] = (
    merged["baseline_avg_per_day"] * 15
)

merged["uplift"] = (
    merged["pongal_qty"] / merged["baseline_15day_qty"]
)

result = merged[merged["uplift"] >= 2].copy()

result = result.sort_values("uplift", ascending=False)

result.to_csv("pongal_avg_4yrs.csv", index=False)

print("pongal_avg_4yrs.csv created")
