from dotenv ipmort load_dotenv
import os
from prompt_toolkit import prompt
import requests

load_dotenv() 


def request_riskiq_api(query: str) -> requests.Response:
    url = 'https://api.riskiq.net/pt/v2/dns/passive'
    user = os.getenv('RISKIQ_USER')
    key = os.getenv('RISKIQ_KEY')
    print()
    auth = (user, key)
    data = {'query': query}
    try:
        r = requests.get(url, auth=auth, json=data)

        return r.json()
    except requests.exceptions.ConnectionError as e:
        print(f'{e}')


def fetch_riskiq_data():
    data = prompt('IP address: ')
    response = request_riskiq_api(query=data)
    print('IP_Pursuit discovered the following on RiskIQ... \n')
    
    for items in response['results']:
        print(f'Resovlved: {items["resolve"]}')

    if items['resolve'] is None:
        print('No resolutions were found')
 
