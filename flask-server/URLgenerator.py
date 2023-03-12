

import string
import random

# alphabetLower = list(string.ascii_lowercase)
# alphabetUpper = list(string.ascii_uppercase)
# print(alphabetLower)
# print(alphabetUpper)

alphabet = list(string.ascii_letters)

def get_random_string(length):
    result_str = ''.join(random.choice(alphabet) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(6)




# >>> def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
# ...    return ''.join(random.choice(chars) for _ in range(size))
# ...
# >>> id_generator()
# 'G5G74W'
# >>> id_generator(3, "6793YUIO")
# 'Y3U'