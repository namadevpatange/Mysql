import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Root@123" )
cursor = mydb.cursor()
s = "insert into Test2.student values(101,'vaibhav','mca')"
cursor.execute(s)
mydb.commit()