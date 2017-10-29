import csv
import MySQLdb
import getpass

# establish a database connection
host = "gwutest.cikpgzqhte4c.us-east-1.rds.amazonaws.com"
user = "dstuckey"
password = getpass.getpass()
database = "workshop"

# read the csv
data = []
with open("../data/us_interest_rates.csv","rb") as csvfile:
    reader = csv.reader(csvfile)
    reader.next() #skip the header
    data = [row for row in reader]

dbcon = MySQLdb.connect(host=host,user=user,passwd=password,db=database)

# release resources after executing queries
with dbcon:
	# create a table to hold the data
	c = dbcon.cursor()
	c.execute("drop table if exists interest_rates ")
	print(c.fetchall())
	c.execute("create table interest_rates (year int, rate double) ")
	print(c.fetchall())

	# import pdb; pdb.set_trace()

	# c.close()
	# c = dbcon.cursor()
	# c.execute("insert into interest_rates (year,rate) values (1,1.1);")

	# insert the data
	c.executemany("INSERT INTO interest_rates (year,rate) VALUES (%s,%s)", data)
	print(c.fetchall())



