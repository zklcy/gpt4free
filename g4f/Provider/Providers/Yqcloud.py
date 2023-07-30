import os
import time
import requests

from ..typing import sha256, Dict, get_type_hints
url = 'https://chat2.jinshutuan.com'
model = [
    'gpt-3.5-turbo',
]
supports_stream = True
needs_auth = False
working = True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):

    headers = {
        'authority': 'api.binjie.fun',
        'origin': 'https://chat2.jinshutuan.com',
        'referer': 'https://chat2.jinshutuan.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    json_data = {
        'prompt': messages[-1]['content'],
        'userId': f'#/chat/{int(time.time() * 1000)}',
        'network': False,
        'apikey': '',
        'system': '',
        'withoutContext': True,
    }

    response = requests.post('https://api.binjie.fun/api/generateStream', headers=headers, json=json_data, stream=True)
    for token in response.iter_content(chunk_size=2046):
        if not b'always respond in english' in token:
            yield (token.decode('utf-8'))

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])


if __name__=="__main__":
    reponse = _create_completion(model="", messages=[ {"role": "user", "content": "hello"}],stream=True)
    for chunk in reponse:
        print(chunk)