# python 线程通信是通过 queue 实现的
# python 多进程两种通信方式：queue、pipe，两种传递的都是 pickle 后的内容
# unix 环境下，python 进程间的 queue 是通过 pipe 实现的。
from multiprocessing import Queue, Process, Pipe

# def echo(from_queue, to_queue):
#     while True:
#         content = from_queue.get()
#         if content == 'EOF':
#             to_queue.put('EOF')
#             return
#         else:
#             print(f'Got: {content}')
#             to_queue.put(content)
# if __name__ == '__main__':
#     from_queue = Queue()
#     to_queue = Queue()
#     p = Process(target=echo, args=(from_queue, to_queue))
#     p.start()
#
#     for i in range(5):
#         from_queue.put(echo)
#         echo = to_queue.get()
#         print(f'echo: {echo}')
#     from_queue.put('EOF')
#     p.join()

def echo(parent_write, parent_read, child_write, child_read):
    parent_read.close()
    parent_write.close()
    while True:
        content = child_read.recv()
        if content == 'EOF':
            child_write.send('EOF')
            return
        else:
            print(f'Got: {content}')
            child_write.send(content)

if __name__ == '__main__':
    parent_write, child_read = Pipe()
    parent_read, child_write = Pipe()
    p = Process(target=echo, args=(parent_write, parent_read, child_write, child_read))
    p.start()

    for i in range(5):
        parent_write.send(echo)
        echo = parent_read.recv()
        print(f'echo: {echo}')
    parent_write.send('EOF')
    p.join()