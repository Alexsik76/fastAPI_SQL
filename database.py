import pymysql.cursors
from pymysql import ProgrammingError

db_credentials = {
    'host': '192.168.88.71',
    'user': 'sql_user',
    'password': 'password',
    'database': 'carshop'
}


def make_query(sql_query):
    connection = pymysql.connect(**db_credentials,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql_query)
                result = cursor.fetchall()
                return result
            except ProgrammingError as error:
                print(error.args)
                return {'error': error.args[1]}
