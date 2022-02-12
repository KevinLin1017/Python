import numpy as np
import pandas as pd
import datetime

# Read user input on what file name they wish to read
# Attempt to read the file
#   if failed as the user to try again
#   if succeeds ask the user for a month and year they wish to see
#   Grab desire data
#   Display data on the screen
#   Bonus: Display steps on console
# 1.
# userInput = input("Please enter the month and the year of the file you want to open : ")

f = open("Log.txt", "w")
fileName = "expedia_report_monthly_march_2018.xlsx"
month = fileName.split("_")[3]
year = (fileName.split("_")[4])[0:4]
month_labels = {
    1: "january",
    2: "feburary",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "october",
    11: "november",
    12: "december",
}

try:
    validInput = True
    f.write(
        "{0} [INFO  ] : Attempting to open file {1}".format(
            datetime.datetime.now(), fileName
        )
    )
    df = pd.read_excel(
        fileName,
        sheet_name="Summary Rolling MoM",
        engine="openpyxl",
    )
except BaseException as err:
    print("Error: The following file {} does not exist".format(err))
    print("The program will now exit.")

df.columns = [
    "Date",
    "Calls Offered",
    "Abandon after 30s",
    "FCR",
    "DSAT",
    "CSAT",
]

df = df.dropna()
df = df.drop(index=12)

df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = (df["Date"].dt.month).apply(lambda x: month_labels[x])
df["Calls Offered"] = df["Calls Offered"].astype(int)
df["Abandon after 30s"] = df["Abandon after 30s"].apply("{:.2%}".format)
df["FCR"] = df["FCR"].apply("{:.2%}".format)
df["DSAT"] = df["DSAT"].apply("{:.2%}".format)
df["CSAT"] = df["CSAT"].apply("{:.2%}".format)

print(df)
print(
    df.loc[
        (df.Month == month) & (df.Year == year),
        [
            "Month",
            "Year",
            "Calls Offered",
            "Abandon after 30s",
            "FCR",
            "DSAT",
            "CSAT",
        ],
    ]
)
