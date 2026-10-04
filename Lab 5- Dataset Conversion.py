#################################################
# Lab 5: Dataset Conversion                     #
# --------------------------------------------- #
# Karla-Aliya' Savon # HSC4933.005 # 10/03/2026 #

import pandas as pd

# Setting the dataset csv file to be referred to as df
df = pd.read_csv("Maternal Health Risk Data Set.csv")

# Naming/ converting csv file to parquet file then creating the rows and columns to that n printing
parquet_file = f"{"Maternal Health Risk Data Set.parquet"}.parquet"
df.to_parquet(parquet_file, engine="pyarrow", index=False)
print(f"Wrote {len(df)} rows to {parquet_file}")

# Naming/ converting csv file to json file then creating the rows to that n printing
Json_file = f"{"Maternal Health Risk Data Set.json"}.json"
df.to_json(Json_file, orient="records", lines=False)
print(f"Wrote {len(df)} rows to {Json_file}")

# Naming/ converting csv file to xlsx file then creating the rows to that n printing
xlsx_file = f"{"Maternal Health Risk Data Set.xlsx"}.xlsx"
df.to_excel(xlsx_file, index=False)
print(f"Wrote {len(df)} rows to {xlsx_file}")