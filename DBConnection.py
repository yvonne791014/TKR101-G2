'''
docker run --name mysql-container -p 3307:3306 -e MYSQL_ROOT_PASSWORD=1234567890 -d mysql:latest
'''

# 引入必要套件
import pymysql

# 設定資料庫連線資訊
host = 'localhost'
port = 3307
user = 'root'
passwd = 'password'
db = 'TESTDB'
charset = 'utf8mb4'


def get_conn():
    conn = pymysql.connect(host=host, port=port, user=user,
                           passwd=passwd, db=db, charset=charset)
