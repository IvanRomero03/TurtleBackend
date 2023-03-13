import string
import random

def randomHash(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
