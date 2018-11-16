# coding:utf-8

import pymysql
import HuShi.Config.mysql_config

class Conn_MySQL:

    def __init__(self):

        self.db_ip = HuShi.Config.mysql_config.ip
        self.db_port = HuShi.Config.mysql_config.port
        self.db_tableName = HuShi.Config.mysql_config.tableName
        self.db_username = HuShi.Config.mysql_config.username
        self.db_pwd = HuShi.Config.mysql_config.password

    def Connect(self,sql,datas=None):
        try:
            conn = pymysql.Connect(self.db_ip,self.db_username,self.db_pwd,self.db_tableName,self.db_port,charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
        except:
            conn.close()

        # 创建游标
        cousor = conn.cursor()
        try:
            rows = cousor.execute(sql)
        except:
            conn.rollback() # 事务回滚

        conn.close()

        return cousor.fetchone()

if __name__ == "__main__":
    sql = "SELECT date_format(create_time,'%Y-%m-%d %H:%i') as result FROM user_opinion WHERE user_id=47 order by create_time DESC LIMIT 1"
    result = Conn_MySQL().Connect(sql)
    print(str(result["result"]))


# # 查询语句
# select_sql = "select id,nickname from edu_user WHERE id in (206660,206667)"
# rows = cousor.execute(select_sql) # 影响的多少行
# # fetchone() 一条数据用它
# # fetchall() 多条数据用它
# result = cousor.fetchall()
# print(result)
#
#
# # 添加一条数据
# add_sql = "insert into edu_user xxx VALUE('xxx','xxx')"
# try:
#     row = cousor.execute(add_sql)
#     conn.commit()
# except:
#     conn.rollback() # 如果失败，事务回滚
#
# conn.close()

"""
列表，元祖：%s 代替
字典： %(name)s 代替
data = [11,"Beckham"]
insert_sql = "insert into test(id,nickname) VALUES (%s,%s)"
#字典
data = {"id":14,"nickname":"xiaojian"}
insert_sql = "insert into test(id,nickname) VALUES (%(id)s,%(nickname)s)"

cousor.execute(insert_sql,data)
"""