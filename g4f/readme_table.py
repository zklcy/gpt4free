import sys
import os
import traceback

from .Provider import (
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

# 可用的Provider
Chat35CanUsedStreamProvider = []
Chat35CanUsedProvider = []
Chat4CanUsedStreamProvider = []
Chat4CanUsedProvider = []

def testAllProvider():
    for provid in providers:
        if not provid.working :
            continue

        def printProvider():
            parsed_url = urlparse(provid.url)
            name = f"`g4f.provid.{provid.__name__.split('.')[-1]}`"
            url = f'[{parsed_url.netloc}]({provid.url})'
            has_gpt4 = '✔️' if 'gpt-4' in provid.model else '❌'
            has_gpt3_5 = '✔️' if 'gpt-3.5-turbo' in provid.model else '❌'
            streaming = '✔️' if provid.supports_stream else '❌'
            needs_auth = '✔️' if provid.needs_auth else '❌'
            
            working = '![Active](https://img.shields.io/badge/Active-brightgreen)' if provid.working else '![Inactive](https://img.shields.io/badge/Inactive-red)'
            
            print(f'| {url} | {name} | {has_gpt3_5} | {has_gpt4} | {streaming} | {working} | {needs_auth} |')

        if 'gpt-3.5-turbo' in provid.model:
            chat35Providers.append(provid)
            printProvider()
        
        
        if 'gpt-4' in provid.model:
            chat4Providers.append(provid)
            printProvider()



    def isError(msg):
            if "error" in msg.lower():
                return True
            return False
        
    def isChat35():
        return 'gpt-3.5-turbo' in provid.model

    def isChat4():
        return 'gpt-4' in provid.model

    def test(model, provid):
        
        print(f"Start Test {provid.__name__} {model}")
        stream = provid.supports_stream
        try:
            response = provid._create_completion(model, [ {"role": "user", "content": "hello"}], stream)

            # response = ChatCompletion.create(model=model, provider=provider, messages=[
            #                                     {"role": "user", "content": "hello"}], stream=stream)

            ret= ""
            if stream:
                for message in response:
                    ret += message
                    print(message)
                if not isError(ret):
                    if isChat35:
                        if provid not in Chat35CanUsedStreamProvider:
                            Chat35CanUsedStreamProvider.append(provid)
                    if isChat4:
                        if provid not in Chat4CanUsedStreamProvider:
                            Chat4CanUsedStreamProvider.append(provid)                    
                else:
                    if provid in Chat35CanUsedStreamProvider:
                         Chat35CanUsedStreamProvider.remove(provid)
                    if provid in Chat4CanUsedStreamProvider:
                         Chat4CanUsedStreamProvider.remove(provid)                                         
            else:
                ret = str(response)
                print(ret)
                if not isError(ret):
                    if isChat35:
                        if provid not in Chat35CanUsedProvider:
                            Chat35CanUsedProvider.append(provid)
                    if isChat4:
                        if provid not in Chat4CanUsedProvider:
                            Chat4CanUsedProvider.append(provid)                            
                else:
                    if provid in Chat35CanUsedProvider:
                         Chat35CanUsedProvider.remove(provid)
                    if provid in Chat4CanUsedProvider:
                         Chat4CanUsedProvider.remove(provid)                                     

        except Exception as e:
            print(e)
            traceback.print_exc()

            if provid in Chat35CanUsedProvider:
                    Chat35CanUsedProvider.remove(provid)
            if provid in Chat4CanUsedProvider:
                    Chat4CanUsedProvider.remove(provid)                                     
            if provid in Chat35CanUsedStreamProvider:
                    Chat35CanUsedStreamProvider.remove(provid)
            if provid in Chat4CanUsedStreamProvider:
                    Chat4CanUsedStreamProvider.remove(provid)                                                             

        finally:
            print("-----------------------------------------------------------------------")        

    for i in chat35Providers:
        test('gpt-3.5-turbo' ,i )
    for i in chat4Providers:
        test('gpt-4' ,i )    

    print(f"Chat35|Streams|{','.join(item.__name__ for item in Chat35CanUsedStreamProvider)}\n")
    print(f"Chat35|{','.join(item.__name__ for item in Chat35CanUsedProvider)}\n")
    print(f"Chat4|Streams|{','.join(item.__name__ for item in Chat4CanUsedStreamProvider)}\n")
    print(f"Chat4||{','.join(item.__name__ for item in Chat4CanUsedProvider)}\n")


if __name__ == "__main__":
    testAllProvider()