import pymysql.cursors
from pymysql import (Error,InterfaceError, DataError, DatabaseError, OperationalError, IntegrityError, InternalError,
                     NotSupportedError, ProgrammingError, MySQLError)

from .config import settings

db_credentials = dict(host=settings.db_host,
                      user=settings.db_user,
                      password=settings.db_password,
                      database=settings.db_name)


def make_query(sql_query):
    connection = pymysql.connect(**db_credentials,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql_query)
                query_result = cursor.fetchall()
                return query_result
            except ProgrammingError as error:
                return {"error": error.args[1]}


def make_insert(sql_query):
    connection = pymysql.connect(**db_credentials,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql_query)
                connection.commit()
                return {"result": "Ok"}
            except (Error,InterfaceError, DataError, DatabaseError, OperationalError, IntegrityError, InternalError,
                    NotSupportedError, ProgrammingError, MySQLError) as error:
                return {"error": error.args[1]}
