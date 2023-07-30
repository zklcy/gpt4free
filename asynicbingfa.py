import g4f

from g4f.Provider import (
    Ails,
    You,
    Bing,
    Yqcloud,
    Theb,
    Aichat,
    Bard,
    Vercel,
    Forefront,
    Lockchat,
    Liaobots,
    H2o,
    ChatgptLogin,
    DeepAi,
    GetGpt,
    AItianhu,
EasyChat,
Acytoo  ,
DfeHub  ,
AiService,
BingHuan,
Wewordle,
ChatgptAi,
Vercel
)

provider = [
    #DeepAi,
    GetGpt,
            ]



ret= []
t = []
num = 3


# Set with provider
async def ask(index):
    for i in provider:
        try:
            print(f"[{index}]:Start asking")
            response = await g4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=i, messages=[
                                                {"role": "user", "content": "写一篇200字的关于人生及时享乐的哲学句子"}], stream=True)

            for message in await response:
                #pass
                print(f"[{index}]:"+message)
                ret[index] += message
            # print(f"---------------------------Work:"+str(i))
        except Exception as e:
            t =str(i)
            print(f"[{index}] Not Work:{t}")
            continue



# def ask(i):
#     chat  = ChatYQ() #ChatZK.get_instance()
#     answer = chat.ask("写一篇200字的关于人生及时享乐的哲学句子")
#     print(f"starting {i}")
#     for line in answer:
#         # print(f"[{i}]:"+line)
#         ret[i] += line

# import threading
async def main():
    for i in range(num):
        ret.append('')
        print(f"Start {i} thread")
        # x = threading.Thread(target=ask,args=(i,))
        await ask(i)
        # ask(i)

        print(f"[{i}]:{ret[i]}")
        # x.start()
        # t.append(x)

    # for i in range(num):
    #     t[i].join()

    # for i in range(num):
    #     print(f"[{i}]:{ret[i]}")
import  asyncio
asyncio.run(main())
