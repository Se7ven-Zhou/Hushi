# coding = utf-8


import pymysql
import HuShi.Config.mysql_config

class CleanData:

    def __init__(self):

        self.db_ip = HuShi.Config.mysql_config.ip
        self.db_port = HuShi.Config.mysql_config.port
        self.db_tableName = HuShi.Config.mysql_config.tableName
        self.db_username = HuShi.Config.mysql_config.username
        self.db_pwd = HuShi.Config.mysql_config.password

    def InitData(self,sql,datas=None):
        try:
            conn = pymysql.Connect(self.db_ip,self.db_username,self.db_pwd,self.db_tableName,self.db_port,charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
        except:
            conn.close()

        # 创建游标
        cousor = conn.cursor()
        try:
            cousor.execute(sql)
            conn.commit()
        except:
            conn.rollback() # 事务回滚

        conn.close()
        print("********** 初始化账号成功 **********")

if __name__ == "__main__":
    SQL = "SELECT coin_num FROM user_operation_record  WHERE user_id=58 AND operation_type_code=02 order by create_time DESC LIMIT 1"
    sql = "DELETE FROM user_operation_record WHERE user_id=58 AND operation_type_code=02 order by create_time DESC LIMIT 1"
    CleanData().InitData(sql)
