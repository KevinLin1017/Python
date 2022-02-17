import pandas as pd
import logging


# Configuration for logging
logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="[%(asctime)s] %(lineno)d [%(levelname)s   :] - %(message)s",
    filemode="w",
    datefmt="%H:%M:%S",
)

# Variable used to convert datetime month to words
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

fileName = "expedia_report_monthly_january_2018.xlsx"
sheetName = "Summary Rolling MoM"
decoder = "openpyxl"
# fileName = "expedia_report_monthly_march_2018.xlsx"


try:
    # File input names
    # fileName = input("Please input the name of the file :")

    # Extract the month from the file name
    month = fileName.split("_")[3]

    # Extract the year from the file name
    year = int((fileName.split("_")[4])[0:4])

    # Open the excel file based on the file name given prior
    # FileName: the file path and name of file
    # SheetName: Which tab of excel sheet
    # engine: Decoding method
    logging.info("Attempting to open file {}".format(fileName))

    df = pd.read_excel(fileName, sheet_name=sheetName, engine=decoder)

    logging.info("File has sucessifully been open")

    # Associated the columns in the excel sheet to the dataframe
    placeHolder = []
    for i in range(len(df.columns)):
        placeHolder.append(df.columns[i].strip())
    placeHolder[0] = "Date"
    df.columns = placeHolder

    logging.debug(" Formating Table ...")

    # The following code formats the table to remove all unused information --------------
    # Drop all the columns/row that contains no values
    df = df.dropna()

    # Remove the row called average
    df = df[df["Date"] != "Average"]

    # Adjust date to a datetime rather than object
    df["Date"] = pd.to_datetime(df["Date"])

    # Obtain the year from Date
    df["Year"] = df["Date"].dt.year

    # Obtain the month from Date
    df["Month"] = (df["Date"].dt.month).apply(lambda x: month_labels[x])

    # Adjust Calls Offered to an interger type
    df["Calls Offered"] = df["Calls Offered"].astype(int)

    # Adjust Abandon after 30s to a percentage
    df["Abandon after 30s"] = df["Abandon after 30s"].apply("{:.2%}".format)

    # Adjust FCR to a percentage
    df["FCR"] = df["FCR"].apply("{:.2%}".format)

    # Adjust DSAT to a percentage
    df["DSAT"] = df["DSAT"].apply("{:.2%}".format)

    # Adjust CSAT to a percentage
    df["CSAT"] = df["CSAT"].apply("{:.2%}".format)
    logging.debug(" Table formmated complete ")

    # ---------------------------------------------------------------------------------------

    # Look for the data the user wants and which column is returned
    result = df.loc[
        (df.Month == month) & (df.Year == year),
        ["Month", "Year", "Calls Offered", "Abandon after 30s", "FCR", "DSAT", "CSAT"],
    ]
    
    # Format the result so they are not in panda series 
    callsOffered = int(result["Calls Offered"].values)
    abandon = str((result["Abandon after 30s"].values)[0])
    fcr =  str((result["FCR"].values)[0])
    dsat = str((result["DSAT"].values)[0])
    csat = str((result["CSAT"].values)[0])
    
    # Log the user's data
    logging.debug(" The request has been processed \n {}".format(result))
    logging.info(" \n\n\n\n{} {} \nCalls Offered: {} \nAbandon after 30s: {} \nFCR: {} \nDSAT: {}\nCSAT: {}".format(month,year,callsOffered,abandon,fcr,dsat,csat))
    print(result)

except BaseException as err:
    logging.debug("Error: The following file {} does not exist".format(err))
    print("The program will now exit.")
    quit()

