from prompt_toolkit import prompt
import json
import requests
import os
from dotenv import load_dotenv


load_dotenv()


def request_binedge_api(target_ip):
    binedge_key = os.getenv("BINEDGE")
    base_url = 'https://api.binaryedge.io/v2/query/ip/'
    headers = {'X-Key': str(binedge_key)}
    
    try:
        response = requests.get(base_url + target, headers=headers)
        return response.json()
    except requests.RequestException as e:
        print(e)


def display_binedge_data():
    data = prompt('IP address: ')
    response = request_binedge_api(target_ip=data)
    api_data = json.dumps(response, indent=4)
    print(api_data)
