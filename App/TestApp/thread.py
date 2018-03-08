
from threading import Thread
from queue import PriorityQueue

queue_login = PriorityQueue()
queue_basicInfo = PriorityQueue()
queue_moreInfo = PriorityQueue()

# 添加后台线程

class login_thread(Thread):
    def run(self, *args, **kwargs):
        while True:
            value = queue_login.get()
            queue_login.task_done()
            print('\nload :' +value)