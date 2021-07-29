"""
对于支持事务的数据库，在Python数据库中，当游标创建时，就自动开始了一个隐形对的数据库事务
commit()方法游标的所有更新操作
rollback()方法回滚当前游标的所有操作
每一个方法都开始了一个新的事务
"""
import pymysql
config = {
    "host":"api.lemonban.com",
    "port":3306,
    "user":"future",
    "password":"123456",
    "database":"futureloan",
    "charset":"utf8",
    "cursorclass":pymysql.cursors.DictCursor  # 将默认的元组格式转换成字典格式输出
}
# 打开数据库连接
conn = pymysql.connect(**config)
# 创建游标
cursor = conn.cursor()
sql = 'select * from member limit 3;'
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
    # 获取单条数据
    one = cursor.fetchone()
    print(one)
    # 获取所有记录列表
    results = cursor.fetchall()

    print(results)
except:
    # 发生错误时回滚
    conn.rollback()

# 关闭数据库，关闭游标
conn.close()
cursor.close()
