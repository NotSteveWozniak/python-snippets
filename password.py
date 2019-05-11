#!/usr/bin/python3

import string
import random

def createrandompassword():
    chars=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return ''.join(random.choice(chars) for x in range(10))


print(createrandompassword())

