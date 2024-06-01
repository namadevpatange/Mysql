import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Root@123" )
cursor = mydb.cursor()
cursor.execute("select * from Test2.student")
for i in cursor.fetchall():
    print( i)