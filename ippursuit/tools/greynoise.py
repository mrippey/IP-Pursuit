from ippursuit.config_setup import CONFIG, load_yml_config
from ippursuit.make_requests import api_call_get
from prompt_toolkit import prompt
import json

key = CONFIG['greynoise']['api']
url = 'https://api.greynoise.io/v3/community/'


def config_exists():
    return load_yml_config()


def get_greynoise_api():
    headers = {'User-Agent': 'IP_Pursuit v0.1 (Research)', 'key': key}
    fields = prompt('[2] Enter an ip address: \n')
    print('IP_Pursuit discoverd the following on GreyNoise: \n')
    data = api_call_get(url + fields, headers=headers)
    result = json.dumps(data, indent=4)
    print(result)

#TODO Parse data for specific output
