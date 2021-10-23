from ippursuit.config_setup import load_yml_config
from prompt_toolkit import prompt
import requests


def config_exists():
    return load_yml_config()


def request_riskiq_api(query: str) -> requests.Response:
    url = 'https://api.riskiq.net/pt/v2/dns/passive'
    user = prompt('Enter your RiskIQ username: ')
    key = prompt('Enter your RiskIQ API key: ')
    print('IP_Pursuit discovered the following on RiskIQ... \n')
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
