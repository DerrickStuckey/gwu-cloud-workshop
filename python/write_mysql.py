## sample script to read data from a CSV and upload to a MySQL Db

import mysqlmod
import pandas as pd

## read the data from a CSV
us_interest_rates = pd.DataFrame.from_csv("../data/us_interest_rates.csv")

## establish a connection
dbcon = mysqlmod.getDBConnect()

## read the table from a CSV
mysqlmod.saveToDB(us_interest_rates, "us_interest_rates2", dbcon, replace=False)


