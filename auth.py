import random
import string
from hashlib import sha1
import time

def create_unique_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def get_timestamp():
    return str(int(time.time()))

def get_hash(caller_id, timestamp, api_key, unique_string):
    return sha1(caller_id + timestamp + api_key + unique_string).hexdigest()
