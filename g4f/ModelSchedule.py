import time
from . import readme_table as  canUsedChatgpt
from datetime import datetime



class Scheduler:    
    GPT35STREAM = 'GPT35STREAM' 
    GPT35='GPT35'
    GPT4STREAM='GPT4STREAM'
    GPT4='GPT4'    
    def __init__(self):
        self.queue={
            self.GPT35STREAM : canUsedChatgpt.Chat35CanUsedStreamProvider,
            self.GPT35:canUsedChatgpt.Chat35CanUsedProvider,
            self.GPT4STREAM : canUsedChatgpt.Chat4CanUsedStreamProvider,
            self.GPT4:canUsedChatgpt.Chat4CanUsedProvider
        }

    def reset_counters(self):
        for obj in self.buffer_pool:
            obj.access_count = 0
        self.last_reset_time = time.time()

    def schedule_objects(self):
        # 每半个小时对所有的模型测试一次，看看是否都可以使用，不能用的就从队列中去除
        while True:
            print(f"--------------------------Start Test All Provider---------------")
            canUsedChatgpt.testAllProvider()
            print(f"--------------------------End Test All Provider---------------")
            time.sleep(1800)  # 半小时

    def get_object_from_queue(self,queue_name):
        queue = self.queue.get(queue_name,None)
        if queue is None:
            print(f"Wrong queue name({queue_name})")
            return None

        if len(queue)<=0:
            print(f"Oops,No provider aviable.")
            return None

        for provider in queue:
            if not hasattr(provider,'_lasttime') or time.time() - provider._lasttime >= 60:
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}]Get Provider {provider.__name__}")
                provider._lasttime = time.time()
                # 放到队尾
                queue.remove(provider)
                queue.append(provider)
                return provider
    
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}]Get Provider {provider.__name__}, {time.time()-provider._lasttime}ms before used")
        #实在找不到就取第一个吧
        provider = queue.pop() 
        provider._lasttime = time.time()
        queue.append(provider)
        return provider

# 示例代码使用时：
scheduler = Scheduler()

def start_scheduler():
    # 启动调度线程
    import threading
    sched_thread = threading.Thread(target=scheduler.schedule_objects)
    sched_thread.daemon = True
    sched_thread.start()

    # import asyncio
    # loop = asyncio.get_event_loop()
    # # Run the coroutine in the event loop
    # loop.run_until_complete(scheduler.schedule_objects())


if __name__ == "__main__":
    while(True):
        time.sleep(60)