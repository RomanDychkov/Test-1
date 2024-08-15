import pymysql
from nameinfo import host, user, password, bd_name

try:
    connection = pymysql.connect(
    host=host,
    user = user,
    password = password,
    database= bd_name,
    cursorclass= pymysql.cursors.DictCursor
    )
    print('победа')
    with connection.cursor() as cursor:
        zapros = 'SELECT age, COUNT(age) FROM relatives GROUP BY age;'
        cursor.execute(zapros)
        ere = cursor.fetchall()
        for i in ere:
            print(i)
except Exception as en:
    print('что-то не получилось')
    print(en)
