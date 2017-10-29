import csv
import MySQLdb
import getpass

# establish a database connection
host = "gwutest.cikpgzqhte4c.us-east-1.rds.amazonaws.com"
user = "dstuckey"
password = getpass.getpass()
database = "workshop"
dbcon = MySQLdb.connect(host=host,user=user,passwd=password,db=database)

with dbcon:
	# execute a query to read the interest rate data
	c = dbcon.cursor()
	c.execute("select * from interest_rates")

	# read the first row of the results
	r1 = c.fetchone()
	print(r1)

	# read the rest of the results
	r2 = c.fetchall()
	print("%i results" % len(r2))
	print(r2)
