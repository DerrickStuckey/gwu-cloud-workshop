# -*- coding: utf-8 -*-
"""
@author: dstuckey
"""
import pandas as pd
import MySQLdb as myDB
from sqlalchemy import create_engine

mysql_host = "gwu-workshop-mysql.cegeieiv8hqw.us-west-2.rds.amazonaws.com"
mysql_user = "derrick"
mysql_pass = ""
mysql_db = "mydb"
mysql_port = 3306

# Function to save a dataframe to CSV
def saveToCsv(df, name):
    df.to_csv(saveDir + '/' + name + '.csv')

def getDBConnect():
    return myDB.connect(host=mysql_host,
                                user=mysql_user,
                                passwd=mysql_pass,
                                db=mysql_db,
                                port=mysql_port)

# Function to save DataFrame to MySQL database
def saveToDB(df, table, dbConnect, replace=False):
    if (replace):
        action='replace'
    else:
        action='append'
    #clean up any 'NaN' fields which mysql doesn't understand
    dfClean = df.where((pd.notnull(df)), None)
    dfClean.to_sql(con=dbConnect,
                    name=table,
                    if_exists=action,
                    flavor='mysql')

# Missing sqlalchemy.schema module
def readFromDB(table, dbConnect):
    engine = create_engine('mysql+mysqldb://' + mysql_user + ':' + mysql_pass + '@' + mysql_host + '/' + mysql_db)
    
    df = pd.read_sql_table(table, con=engine)
    #clean up SUBJ column
    #df.SUBJ = df.SUBJ.str.strip()
    return df
