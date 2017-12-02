import ConfigParser
import auth
from web_client import WebClient

configParser = ConfigParser.ConfigParser()
configParser.read('booli.config')

host = configParser.get('auth', 'host')
caller_id = configParser.get('auth', 'caller_id')
api_key = configParser.get('auth', 'api_key')

print 'Collecting data from {} with caller id {}'.format(host, caller_id)

client = WebClient(host, caller_id, api_key)
print client.get('/listings?q=nacka')

