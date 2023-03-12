
import string
import random


def generate_short_url(longURL: str):
    alphabet = list(string.ascii_letters)
    counter = 0
    shortURL = ""

    while counter < 6:
        shortURL = shortURL + random.choice(alphabet)
        counter = counter + 1
    
    print(shortURL)

generate_short_url("www.google.com")





#Notes:
# alphabetLower = list(string.ascii_lowercase)
# alphabetUpper = list(string.ascii_uppercase)
# print(alphabetLower)
# print(alphabetUpper)