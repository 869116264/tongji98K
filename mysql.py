import pymysql
import sys

sys.path.append(r'/Users/fanzixiao/PycharmProjects/spider/lib')
from lib import FMysql

mysql = FMysql.FMysql()

array={'title':'test','content':'qwefeadsfada','time':'2017-01-01','id':2,}

# mysql.update(array,"id = 12","software_engineering")
# mysql.create(array,"software_engineering")
# print(mysql.readAll("software_engineering"))
condition={'id':1}
# print(mysql.readAllByWhere("software_engineering",condition))
print(mysql.isUrlExist("software_engineering",1))

if not mysql.isUrlExist("software_engineering",1):
    print("ok")

