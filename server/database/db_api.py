import mysql.connector
from mysql.connector import Error


class DbApi:

    def __init__(self):
        try:
            self._connection = mysql.connector.connect(host='sql9.freesqldatabase.com',
                                                       database='sql9605105',
                                                       user='sql9605105',
                                                       password='m8yprJWXw3')
            if self._connection.is_connected():
                db_Info = self._connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
            self._cursor = self._connection.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._connection.is_connected():
            self._connection.commit()
            self._cursor.close()
            self._connection.close()
            print("MySQL connection is closed")

    def query_tables(self):
        self._cursor.execute("SHOW TABLES")

        for table_name in self._cursor:
            print(table_name)


# try:
#     connection = mysql.connector.connect(host='sql9.freesqldatabase.com',
#                                          database='sql9605105',
#                                          user='sql9605105',
#                                          password='m8yprJWXw3')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()

#         cursor.execute("SHOW TABLES")

#         for table_name in cursor:
#             print(table_name)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
