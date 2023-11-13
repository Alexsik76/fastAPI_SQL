import pymysql.cursors

db_credentials = {
    'host': '192.168.88.252',
    'user': 'sql_user',
    'password': 'password',
    'database': 'carshop'
}
# connection = pymysql.connect(**db_credentials,
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)


def make_query(sql_query):
    connection = pymysql.connect(**db_credentials,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    # print('query: ', sql_query)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
            return result
