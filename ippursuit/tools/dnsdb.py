from dotenv import load_dotenv
from prompt_toolkit import prompt
import json
import requests
import os

load_dotenv()


def request_dnsdb_api(target):
    dnsdb_key = os.getenv("DNSDB")
    headers = {'X-API-KEY': dnsdb_key, 'Accept': 'application/x-ndjson'}
    #target = prompt('ip: ')
    base_url = 'https://api.dnsdb.info/dnsdb/v2/lookup/rdata/ip/'
    try:
        response = requests.get(base_url + target + '/ANY', headers=headers)
        return response.content.decode('utf-8')
    except Exception:
        print('')


def fetch_dnsdb_data():
    target = prompt('IP address: ')
    r = request_dnsdb_api(target=target)
    print(json.dumps(r))
