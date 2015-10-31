## Write some data to an AWS MySQL Instance ##

install.packages("RMySQL")
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

interest_rates <- read.csv("../data/us_interest_rates.csv")
head(interest_rates)

dbWriteTable(mydb, name='us_interest_rates', value=interest_rates,
             row.names=FALSE, overwrite=TRUE)

dbDisconnect(mydb)

