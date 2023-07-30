import sys,os
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, "..")
sys.path.append(relative_path)

import time
from testing import readme_table as canUsedChatgpt




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
            canUsedChatgpt.testAllProvider()
            time.sleep(1800)  # 半小时

    def get_object_from_queue(self,queue_name):
        queue = self.queue.get(queue_name,None)
        if queue is None:
            print(f"Wrong queue name({queue_name})")
            return None

        if len(queue)<=0:
            print(f"Oops,No one can use.")
            return None

        for provider in queue:
            if not hasattr(provider,'_lasttime') or time.time() - self._lasttime >= 60:
                print(f"get provider {provider.__name__}")
                provider._lasttime = time.time()
                # 放到队尾
                queue.remove(provider)
                queue.append(provider)
                return provider
    
        print(f"get provider {provider.__name__}, {time.time()-self._lasttime}ms before used")
        #实在找不到就取第一个吧
        provider = queue.pop() 
        provider._lasttime = time.time()
        queue.append(provider)
        return provider
    

# 示例代码使用时：
scheduler = Scheduler()

# 启动调度线程
import threading
sched_thread = threading.Thread(target=scheduler.schedule_objects)
sched_thread.daemon = True
sched_thread.start()

if __name__ == "__main__":
    while(True):
        time.sleep(60)