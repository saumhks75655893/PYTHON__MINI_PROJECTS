import mysql.connector as sql
con = sql.connect(host="localhost",user="root",passwd="75655893", database="Stdent")

if(con.is_connected()):
    print("Successfully connected....")


