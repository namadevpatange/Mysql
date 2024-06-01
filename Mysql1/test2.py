import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Root@123" )
cursor = mydb.cursor()
s = "create table Test2.student(std_id int(10)  , std_name varchar(80) , std_class varchar(20))"
cursor.execute(s)
mydb.commit()