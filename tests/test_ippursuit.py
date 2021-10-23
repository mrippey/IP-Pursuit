from ippursuit import __version__
from ippursuit.config_setup import CONFIG

def test_version():
    assert __version__ == '0.1.0'


def test_greynoise_equals_200():
    key = CONFIG['greynoise']['api']
    headers = {'key': key}
    r = requests.request("GET", https://greynoise.io/v3/community/1.1.1.1', headers=headers)

    assert r.headers['Content-Type'] == 'application/json'
