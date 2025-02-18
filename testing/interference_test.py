import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, "..")
sys.path.append(relative_path)

import openai

openai.api_key = ''
openai.api_base = 'http://localhost:1337'

chat_completion = openai.ChatCompletion.create(stream=True,
    model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'write a poem about a tree'}])

#print(chat_completion.choices[0].message.content)

for token in chat_completion:
    
    content = token['choices'][0]['delta'].get('content')
    if content != None:
        print(content)