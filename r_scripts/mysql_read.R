## Read some data from an AWS MySQL Instance ##

library(RMySQL)

mysql_host <- "gwu-workshop-mysql.cegeieiv8hqw.us-west-2.rds.amazonaws.com"
mysql_user <- "derrick"
mysql_pass <- ""
mysql_dbname <- "mydb"
mysql_port <- 3306

mydb = dbConnect(MySQL(), 
                 user=mysql_user, 
                 password=mysql_pass, 
                 dbname=mysql_dbname, 
                 host=mysql_host,
                 port=mysql_port)

dbListTables(mydb)
dbListFields(mydb, 'us_interest_rates')

# read the first row of the table
results = dbSendQuery(mydb, "select * from us_interest_rates")
first_row = fetch(results, n=1)
first_row

dbClearResult(results)

# read the whole table
results2 = dbSendQuery(mydb, "select * from us_interest_rates")
full_table <- fetch(results2, n=-1)
nrow(full_table)
head(full_table)
dbClearResult(results2)

dbDisconnect(mydb)


