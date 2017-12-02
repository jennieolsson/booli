import requests
import auth

class WebClient():
    def __init__(self, host, caller_id, api_key):
        self.host = host
        self.caller_id = caller_id
        self.api_key = api_key
    
    def create_auth_string(self):
        unique_string = auth.create_unique_string(16)
        timestamp = auth.get_timestamp()
        hash_str = auth.get_hash(self.caller_id, timestamp, self.api_key, unique_string)
        return '&callerId={}&time={}&unique={}&hash={}'.format(self.caller_id, timestamp, unique_string,hash_str)

    def get(self, path):
        path = self.host + path + self.create_auth_string()
        r = requests.get(path)
        return r.content
