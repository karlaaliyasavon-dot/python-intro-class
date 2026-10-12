################################################
# ------ Lab 7: Linear Regression Lab -------- #
# -------------------------------------------- #
# Karla-Aliya' Savon | karlaaliyasavon@usf.edu #
# -------------- 10/11/2026 ------------------ #
# -------------------------------------------- #
# (C) K-A'. Savon, 2026 | For research         #
################################################

# Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Environment variables
CSV_PATH = "birthwt.csv"
CSV_PATH = "places_2025.csv"

# Prompting user for their choice of dataset
dataset_name = input("Enter dataset birthwt.csv or places_2025.csv: ")

df = pd.read_csv("birthwt.csv")
if dataset_name == "birthwt.csv":

    # print csv stats before cleaning
    print(df.shape,
          df.dtypes,
          df.isna().sum(),
          df.nunique(),
          sep="\n")

    # Print number of duplicated values
    print("Duplicated: ", df.duplicated().sum())

    # Drop columns with no data (only low)
    (df != 0).any(axis=0)
    cols = ["low", "age", "lwt", "race", "smoke", "ptl", "ht", "ui", "ftv", "bwt"]

    # Make column headers snake_case
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Prompting users to choose column name for the X and Y variables
    X_COL = input("Enter the column name you want to use as the X-Variable: ")
    Y_COL = input("Enter the column name you want to use as the Y-Variable: ")
    X = df[X_COL]
    Y = df[Y_COL]
    print(f"You selected {X_COL} and {Y_COL} as your variables ")

    #creating scatterplot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df[X_COL], df[Y_COL], alpha=0.6, edgecolor="k", linewidth=0.3)
    ax.set_xlabel(X_COL)
    ax.set_ylabel(Y_COL)
    ax.set_title(f"{Y_COL} vs {X_COL} (n = {len(df)})")
    ax.grid(alpha=0.3)
    fig.tight_layout()

    #Asking user if they want to save scatterplot
    scatter_file = input("Want to save the scatter plot? (y/n): ")
    if scatter_file == "y":
        # Creating custom file name
        custom_name = input("Enter a custom file name (without extension): ")
        scatter_file = f"{custom_name}.png"
        fig.savefig(scatter_file, dpi=300)

        print(f"Saved scatterplot -> {scatter_file}")

        # Asking if user wants to save scatterplot with OLS Regression line
        scatter_file = input("Want to save the scatter plot with an OLS Regression line? (y/n): ")
        if scatter_file == "y":
            # Convert to numeric
            df[X_COL] = pd.to_numeric(df[X_COL], errors="coerce")
            df[Y_COL] = pd.to_numeric(df[Y_COL], errors="coerce")
            data = df.dropna(subset=[X_COL, Y_COL])

            # perform linear regression
            X = pd.DataFrame(data[X_COL])
            X = sm.add_constant(X)
            model = sm.OLS(df[Y_COL], X).fit()

            # print regression
            print("OLS Regression Summary: ")
            print(model.summary())

            # new scatterplot with regression line
            x_line = np.linspace(df[X_COL].min(), df[X_COL].max(), 100)
            y_line = model.params["const"] + model.params[X_COL] * x_line
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.plot(x_line, y_line, color="crimson", linewidth=2, label=f"OLS line (R2 = {model.rsquared:.3f})")
            ax.set_title(f"{Y_COL} vs {X_COL} (n = {len(df)})")
            ax.legend()

            # Saving file with custom name
            custom_name = input("Enter a custom file name for the regression plot (without extension): ")
            ols_file = f"{X_COL}_vs_{Y_COL}.png"
            fig.savefig(ols_file, dpi=300)
            print(f"Saved OLS plot -> {ols_file}")

            plt.show()



df = pd.read_csv("places_2025.csv")
if dataset_name == "places_2025.csv":

    # print csv stats before cleaning
    print(df.shape,
        df.dtypes,
        df.isna().sum(),
        df.nunique(),
        sep="\n")

    # Print number of duplicated values
    print("Duplicated: ", df.duplicated().sum())

    #Drop columns with no data
    df = df.dropna(axis=1, how="all")
    df = df.dropna()

    # Make column headers snake_case
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    print(df.columns.tolist())

    # Prompting users to choose column name for the X and Y variables
    X_COL = input("Enter the column name you want to use as the X-Variable: ")
    Y_COL = input("Enter the column name you want to use as the Y-Variable: ")
    X = df[X_COL]
    Y = df[Y_COL]
    print(f"You selected {X_COL} and {Y_COL} as your variables ")

    #creating scatterplot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df[X_COL], df[Y_COL], alpha=0.6, edgecolor="k", linewidth=0.3)
    ax.set_xlabel(X_COL)
    ax.set_ylabel(Y_COL)
    ax.set_title(f"{Y_COL} vs {X_COL} (n = {len(df)})")
    ax.grid(alpha=0.3)
    fig.tight_layout()

    #Asking user if they want to save scatterplot
    scatter_file = input("Want to save the scatter plot? (y/n): ")
    if scatter_file == "y":
        # Creating custom file name
        custom_name = input("Enter a custom file name (without extension): ")
        scatter_file = f"{custom_name}.png"
        fig.savefig(scatter_file, dpi=300)

        print(f"Saved scatterplot -> {scatter_file}")

        # Asking if user wants to save scatterplot with OLS Regression line
        scatter_file = input("Want to save the scatter plot with an OLS Regression line? (y/n): ")
        if scatter_file == "y":

            # Convert to numeric
            df[X_COL] = pd.to_numeric(df[X_COL], errors="coerce")
            df[Y_COL] = pd.to_numeric(df[Y_COL], errors="coerce")
            data = df.dropna(subset=[X_COL, Y_COL])

            # perform linear regression
            X = pd.DataFrame(data[X_COL])
            X = sm.add_constant(X)
            model = sm.OLS(df[Y_COL], X).fit()

            # print regression
            print("OLS Regression Summary: ")
            print(model.summary())

            # new scatterplot with regression line
            x_line = np.linspace(df[X_COL].min(), df[X_COL].max(), 100)
            y_line = model.params["const"] + model.params[X_COL] * x_line
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.plot(x_line, y_line, color="crimson", linewidth=2, label=f"OLS line (R2 = {model.rsquared:.3f})")
            ax.set_title(f"{Y_COL} vs {X_COL} (n = {len(df)})")
            ax.legend()

            # Saving file with custom name
            custom_name = input("Enter a custom file name for the regression plot (without extension): ")
            ols_file = f"{X_COL}_vs_{Y_COL}.png"
            fig.savefig(ols_file, dpi=300)
            print(f"Saved OLS plot -> {ols_file}")

            plt.show()





