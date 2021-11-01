from dotenv import load_dotenv
import os
from prompt_toolkit import prompt
import shodan 

load_dotenv()


def request_shodan_api():
    shodan_env = os.getenv('SHODAN')
    api_key = shodan.Shodan(shodan_env)
    target_ip = prompt('IP address: ')
    print(f'Querying Shodan for port & banner information for {target_ip}')
    try:
        shodan_data = api_key.host(target_ip)

        print()
        for item in shodan_data['data']:
            print(f"""
            Port: {item["port"]} 
            Banner: {item["data"]}
            """)

    except shodan.APIError as err:
        print(f'[-] Error: {err}')
