from database.db_api import DbApi
import string
import random


class URLGenerator:

    def __init__(self) -> None:
        pass

    def _generate_short_url(self, longURL: str) -> str:
        alphabet = list(string.ascii_letters)
        counter = 0
        shortURL = ""

        while counter < 6:
            shortURL = shortURL + random.choice(alphabet)
            counter = counter + 1

        return shortURL

    def insert_short_url(self, longURL: str) -> str:
        with DbApi() as db:
            short_url_if_long_url = db.long_url_exists(longURL)
            if short_url_if_long_url != None:
                return short_url_if_long_url
            else:
                new_short_url = self._generate_short_url(longURL)
                while db.short_url_exists(new_short_url):
                    new_short_url = self._generate_short_url(longURL)

                db.insert_url(new_short_url, longURL)

        return new_short_url
