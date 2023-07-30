import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, "..")
sys.path.append(relative_path)

import traceback

import g4f

from g4f.Provider import (
Acytoo,             
Aichat,             
Ails,               
AiService,          
AItianhu,           
Bard,               
Bing,               
BingHuan,           
ChatgptAi,          
ChatgptLogin,       
DeepAi,             
DfeHub,             
EasyChat,           
Forefront,          
GetGpt,             
H2o,                
Liaobots,           
Lockchat,           
Theb,               
Vercel,             
Wewordle,           
You,                
Yqcloud,                  
)

from urllib.parse import urlparse

providers = [
Acytoo,             
Aichat,             
Ails,               
AiService,          
AItianhu,           
Bard,               
Bing,               
BingHuan,           
ChatgptAi,          
ChatgptLogin,       
DeepAi,             
DfeHub,             
EasyChat,           
Forefront,          
GetGpt,             
H2o,                
Liaobots,           
Lockchat,           
Theb,               
Vercel,             
Wewordle,           
You,                
Yqcloud,  
]

# | Website| Provider| gpt-3.5-turbo | gpt-4 | Supports Stream | Status | Needs Auth |
print('| Website| Provider| gpt-3.5 | gpt-4 | Streaming | Status | Auth |')
print('| --- | --- | --- | --- | --- | --- | --- |')

chat35Providers = []
chat4Providers = []

for provider in providers:
    if not provider.working :
        continue

    def printProvider():
        parsed_url = urlparse(provider.url)
        name = f"`g4f.Provider.{provider.__name__.split('.')[-1]}`"
        url = f'[{parsed_url.netloc}]({provider.url})'
        has_gpt4 = '✔️' if 'gpt-4' in provider.model else '❌'
        has_gpt3_5 = '✔️' if 'gpt-3.5-turbo' in provider.model else '❌'
        streaming = '✔️' if provider.supports_stream else '❌'
        needs_auth = '✔️' if provider.needs_auth else '❌'
        
        working = '![Active](https://img.shields.io/badge/Active-brightgreen)' if provider.working else '![Inactive](https://img.shields.io/badge/Inactive-red)'
        
        print(f'| {url} | {name} | {has_gpt3_5} | {has_gpt4} | {streaming} | {working} | {needs_auth} |')

    if 'gpt-3.5-turbo' in provider.model:
        chat35Providers.append(provider)
        printProvider()
    
    
    if 'gpt-4' in provider.model:
        chat4Providers.append(provider)
        printProvider()


def test(model, provider):
    print(f"Start Test {provider.__name__} {model}")
    stream = provider.supports_stream
    try:
        response = g4f.ChatCompletion.create(model=model, provider=provider, messages=[
                                            {"role": "user", "content": "hello"}], stream=stream)

        if stream:
            for message in response:
                print(message)
        else:
            print(response)
    except Exception as e:
        print(e)
        traceback.print_exc()
    finally:
        print("-----------------------------------------------------------------------")        

for i in chat35Providers:
    test('gpt-3.5-turbo' ,i )
for i in chat4Providers:
    test('gpt-4' ,i )    
