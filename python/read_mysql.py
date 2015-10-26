
## establish a connection
dbcon = mysqlmod.getDBConnect()

## read the table
us_interest_rates = readFromDB("us_interest_rates", dbcon)

## print the first row
print(us_interest_rates[1,])

