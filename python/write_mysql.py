import csv
import MySQLdb

# establish a database connection
host = "gwu-test-oct7.cikpgzqhte4c.us-east-1.rds.amazonaws.com"
user = "dstuckey"
password = "gwutestoct7"
database = "workshop"
dbcon = MySQLdb.connect(host=host,user=user,passwd=password,db=database)

# create a table to hold the data
c = dbcon.cursor()
c.execute("create table interest_rates (year int, rate double) ")

# read the csv
with open("./gwu-cloud-workshop/data/us_interest_rates.csv","rb") as csvfile:
    reader = csv.reader(csvfile)
    reader.next() #skip the header
    data = [row for row in reader]

# insert the data
c.executemany("INSERT INTO interest_rates (year,rate) VALUES (%s,%s)", data )



