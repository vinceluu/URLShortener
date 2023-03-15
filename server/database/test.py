# insert and query the rows

from db_api import DbApi  # From db_api file import the DbApi class

# Context manager: Creates the object, executes the function called, calles exit function and closes the object
with DbApi() as db:  # db = DbApi()
    # db.query_tables()
    # db.query_all_URL()
    # db.insert_URL(longURL="www.fb.com", shortURL="eRaEnp")
    db.query_all_url()
    # db.long_url_exists("www.google.com")
    db.short_url_exists("DefSwe")
