import json

def get_login_credentials():
    with open('config/config.json') as config_file:
        config = json.load(config_file)
    return config['username'], config['password']

