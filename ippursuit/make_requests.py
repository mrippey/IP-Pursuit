import requests


def generic_api_request(api_url, headers=None):
    if headers is None:
        headers = {}

    try:
        r = requests.request("GET", api_url)
    except requests.exceptions.RequestException as err1:
        raise(f'{r}: {err1}')
    except requests.exceptions.Timeout:
        raise(f'Request timed out for {r}')

    if 'application/json' in r.headers.get('Content-Type'):
        return r.json()
    else:
        print('Converting data to JSON failed...')
    
    return api_call.content
