import json

def get_creds():
    with open("../config.json",'r') as f:
        config = json.load(f)
        return config['creds']
