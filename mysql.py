import pymysql

db=pymysql.connect("localhost","root","12345Fzx","tongji98k")
cursor=db.cursor()
cursor.execute("SHOW DATABASES")
# data = cursor.fetchall()
cursor.execute("use tongji98k")
# data=cursor.fetchall()
# print(data)
db.close()