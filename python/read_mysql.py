## sample script to read 'us_interest_rates' table from a MySQL DB

import mysqlmod

## read the table
us_interest_rates = mysqlmod.readFromDB("us_interest_rates")

## print the first row
print(us_interest_rates.head())

