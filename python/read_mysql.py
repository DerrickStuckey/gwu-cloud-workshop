
import mysqlmod

## establish a connection
dbcon = mysqlmod.getDBConnect()

## read the table
us_interest_rates = mysqlmod.readFromDB("us_interest_rates", dbcon)

## print the first row
print(us_interest_rates.head())

