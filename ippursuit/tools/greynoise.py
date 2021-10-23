from ippursuit.config_setup import CONFIG, load_yml_config
from ippursuit.make_requests import generic_api_request
from prompt_toolkit import prompt
import json

key = CONFIG['greynoise']['api']
url = 'https://api.greynoise.io/v3/community/'


def config_exists():
    return load_yml_config()


def request_greynoise_api():
    headers = {'User-Agent': 'IP_Pursuit v0.1 (Research)', 'key': key}
    target = prompt('[2] Enter an ip address: \n')
    print('IP_Pursuit discovered the following on GreyNoise... \n')
    req_api_data = generic_api_request(url + target, headers=headers)
    data  = json.dumps(req_api_data, indent=4)
    print(data)

#TODO Parse data for specific output
