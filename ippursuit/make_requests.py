import requests


def api_call_get(api_url, headers=None):
    if headers is None:
        headers = {}

    try:
        api_call = requests.request("GET", api_url)
    except requests.exceptions.RequestException as err1:
        raise(f'{api_url}: {err1}')
    except requests.exceptions.Timeout:
        raise(f'Request timed out for {api_url}')

    if 'application/json' in api_call.headers.get('Content-Type'):
        return api_call.json()
    else:
        print('Converting data to JSON failed...')
    
    return api_call.content
