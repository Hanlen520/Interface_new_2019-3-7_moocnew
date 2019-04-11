
import pymysql

class connectMySQL(object):
    def __init__(self, hostname, user, password, dbname, port):
        db_config = {
            'host': hostname,
            'port': port,
            'user': user,
            'password': password,
            'db': dbname
        }
        self.conn = pymysql.connect(**db_config,charset='utf8')
    """获取游标"""
    def get_cursor(self):
        return self.conn.cursor()
    """查询数据"""
    def querydb(self, sqlstring):
        cursor = self.get_cursor()
        try:
            cursor.execute(sqlstring)
            results = cursor.fetchall()
            for row in results:
                print(row)
        except:
            self.logger.error('Error:unable to fetch data')
if __name__ == '__main__':
    c = connectMySQL('localhost','root','root','guest',3306)
    c.querydb('''SELECT * from `event`''')