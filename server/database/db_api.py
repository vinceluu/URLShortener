import mysql.connector
from mysql.connector import Error


class DbApi:

    def __init__(self):
        try:
            self._connection = mysql.connector.connect(host='sql9.freesqldatabase.com',
                                                       database='sql9608550',
                                                       user='sql9608550',
                                                       password='vTY2Vfci4P')
            if self._connection.is_connected():  # If its private make it _connection
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

    # Implement insertURL: Needs shortURL, longURL. Insert a whole row into the DB
    def insert_url(self, shortURL: str, longURL: str):
        # f will format it to a string
        query = f"INSERT INTO URL_Table (long_url, short_url) VALUES ('{longURL}', '{shortURL}')"
        print(query)
        self._cursor.execute(query)

    def query_all_url(self):
        # self._cursor has all of the rows from URL_Table
        self._cursor.execute("SELECT * FROM URL_Table")
        print("Getting all rows from URL table")
        myresult = self._cursor.fetchall()

        for row in myresult:
            print(row)

    # create query_all_shorturl

    def long_url_exists(self, long_url: str) -> str | None:
        # if long url exists it should return short url
        checkLongURL = f"SELECT long_url, short_url FROM URL_Table WHERE long_url= '{long_url}'"
        # print(checkLongURL)
        self._cursor.execute(checkLongURL)
        myResult = self._cursor.fetchall()
        # print(myResult)
        if self._cursor.rowcount != 0:
            return myResult[0][1]
        else:
            return None

    def short_url_exists(self, short_url: str) -> str | None:
        # select * from where short_url (column) == short_url (value that they are passing)
        checkShortURL = f"SELECT long_url, short_url FROM URL_Table WHERE short_url = '{short_url}'"
        self._cursor.execute(checkShortURL)
        myResult = self._cursor.fetchall()
        if self._cursor.rowcount != 0:
            return myResult[0][0]
        else:
            return None


# try:
#     connection = mysql.connector.connect(host='sql9.freesqldatabase.com',
#                                          database='sql9605105',
#                                          user='sql9605105',
#                                          password='m8yprJWXw3')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()

#         cursor.execute("SHOW TABLES") #SHOW TABLES is a SQL query

#         for table_name in cursor:
#             print(table_name)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
