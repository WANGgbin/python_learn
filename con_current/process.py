# process 行为与平台有关

# Process 对象定义了 _bootstrap 方法，当使用fork()拉起新的进程后，进程便执行Process对象 _bootstrap
# _bootstrap 则调用 Process.run()方法。Process.run() 则调用 target方法。

# terminate 和 kill 方法通过给子进程发送信号来终止子进程
# join  通过调用 Process 的 _popen 成员的 wait 方法，等待子进程结束，该方法本质上是通过系统调用waitpid()
# 等待子进程结束。如果是非阻塞的 wait，调用 waitpid 需要是用选项 WNOHANG

# is_alive 本质上通过非阻塞 os.waitpid() 实现
# close() 用来释放资源，fork 场景下，主要用来释放打开读写描述符
# exitcode 用来获取子进程的退出码



from multiprocessing import Process
import time
import os
from threading import current_thread, Thread
class Test:
    def __init__(self):
        self.members = []
        self.p = Process(target=self.handle)
        self.p.start()
    def handle(self):
        pid = os.getpid()
        print(f'{os.getpid()} start processing...')
        print(f'{pid}: {self.members}')
        self.members.append(pid)
        print(f'{pid}: {self.members}')

def run():
    print(f'create pid: {os.getpid()}')

if __name__ == '__main__':
    while True :
        p = Process(target=run)
        p.start()
        p.join()