# 介绍进程与线程间的同步原语

from multiprocessing import Process

def run():
    while True:
        print('child')

if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    while True:
        print('parent')