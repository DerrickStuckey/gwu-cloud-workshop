import csv
import MySQLdb

# establish a database connection
host = "gwu-test-oct7.cikpgzqhte4c.us-east-1.rds.amazonaws.com"
user = "dstuckey"
password = "gwutestoct7"
database = "workshop"
dbcon = MySQLdb.connect(host=host,user=user,passwd=password,db=database)

# execute a query to read the interest rate data
c = dbcon.cursor()

# read the first row of the results
r1 = c.fetchone()
print(r1)

# read the rest of the results
r2 = c.fetchall()
print("%i results" % len(r2))
print(r2)