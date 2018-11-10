
import pymysql
import sys

print(sys.stdin.encoding)

conn = pymysql.connect(host='localhost', port=3306, user='test', passwd='test123', db='test', charset='utf8')

cur = conn.cursor()
cur.execute("select * from users")

for row in cur:
    print(row[0])


sql = """insert into users(id, user_login, user_pass, age) values(30,'test', 'test5', 30)"""
cur.execute(sql)
conn.commit()

cur.close()
conn.close()







