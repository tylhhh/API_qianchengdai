import pymysql
from Common.handle_config import conf
class HandleDB:

    def __init__(self):
        # 1、连接数据库
        self.conn = pymysql.connect(
            host=conf.get("mysql","host"),
            port=conf.getint("mysql","port"),
            user=conf.get("mysql","user"),
            password=conf.get("mysql","password"),
            database=conf.get("mysql","database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        # 2、创建游标
        self.cur = self.conn.cursor()

    def select_one_data(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all_data(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self,sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def update(self,sql):
        """
        对数据库进行增、删、改的操作。
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()




