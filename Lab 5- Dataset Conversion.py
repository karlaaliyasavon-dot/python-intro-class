#################################################
# Lab 5: Dataset Conversion                     #
# --------------------------------------------- #
# Karla-Aliya' Savon # HSC4933.005 # 10/03/2026 #

import pandas as pd

df = pd.read_csv("Maternal Health Risk Data Set.csv")

parquet_file = f"{"Maternal Health Risk Data Set.parquet"}.parquet"
df.to_parquet(parquet_file, engine="pyarrow", index=False)
print(f"Wrote {len(df)} rows to {parquet_file}")

Json_file = f"{"Maternal Health Risk Data Set.json"}.json"
df.to_json(Json_file, orient="records", lines=False)
print(f"Wrote {len(df)} rows to {Json_file}")

xlsx_file = f"{"Maternal Health Risk Data Set.xlsx"}.xlsx"
df.to_excel(xlsx_file, index=False)
print(f"Wrote {len(df)} rows to {xlsx_file}")