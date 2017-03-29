import os
import configparser
import ipdb
assert os.path.exists('secret.conf'), 'Config error'
parser = configparser.ConfigParser()
parser.read('secret.conf')
AppID = parser.get('wx', 'AppID')
AppSecret = parser.get('wx', 'AppSecret')
Token = parser.get('wx', 'Token')
EncodingAESKey = parser.get('wx', 'EncodingAESKey')
