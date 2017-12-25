import pymysql
import traceback


class FMysql:
    def __init__(self, host="localhost", name="root", password="12345Fzx", dbname="tongji98k"):
        self.db = pymysql.connect(host, name, password, dbname)
        self.cursor = self.db.cursor()
        self.dbname = dbname
        self.execute("use " + self.dbname)

    def __del__(self):
        self.db.close()

    def __getCondition(self, tuple_condition):
        condition = ""
        for column in tuple_condition:
            condition += str(column)
            condition += "='" + str(tuple_condition[column]) + "',"

        condition = condition.rstrip(',')
        return condition

    def __getColumns(self, tuple_columns):
        columns = ""
        for column in tuple_columns:
            columns += str(column)
            columns += ","
        columns = columns.rstrip(',')
        return columns

    def execute(self, sql):
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()

        except Exception:
            self.db.rollback()
            traceback.print_exc()
            # print('Error:',Exception)

    def create(self, dict, table):
        sql = "INSERT INTO " + table
        columns = "("
        values = "("
        for column in dict:
            columns += str(column)
            columns += ","
            values += "'" + str(dict[column]) + "'"
            values += ","
        columns = columns.rstrip(',')
        values = values.rstrip(',')
        columns += ')'
        values += ')'
        sql += columns
        sql += " VALUES "
        sql += values
        self.execute(sql)

    def update(self, set_dict, condition_dict, table):
        sql = "UPDATE " + table + " SET "
        for column in set_dict:
            sql += str(column)
            sql += "='" + str(set_dict[column]) + "',"

        sql = sql.rstrip(',')
        sql += " WHERE " + self.__getCondition(condition_dict)
        self.execute(sql)

    def readAllByWhere(self, table, condition_dict):
        sql = "select * from " + table + " WHERE " + self.__getCondition(condition_dict)
        self.execute(sql)
        return self.cursor.fetchall()

    def readAll(self, table):
        sql = "select * from " + table + ""
        self.execute(sql)
        return self.cursor.fetchall()

    def readSomeByWhere(self, columns_tuple, table, condition_dict):
        sql = "select " + self.__getColumns(columns_tuple) + " from " + table + self.__getCondition(
            condition_dict)
        self.execute(sql)
        return self.cursor.fetchall()

    def readSome(self, columns_tuple, table):
        sql = "select " + self.__getColumns(columns_tuple) + " from " + table
        self.execute(sql)
        return self.cursor.fetchall()

    def delete(self, table, condition):
        sql = "DELETE FROM " + table
        sql += " WHERE " + self.__getCondition(condition)

    def isUrlExist(self,table,url):
        sql="select count(*) from "+table+" WHERE id = "+str(url)
        self.execute(sql)
        return self.cursor.fetchone()[0]


