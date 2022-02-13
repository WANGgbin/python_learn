from queue import Queue, Empty
from .itemObject import item
from .futureObject import future, CANCLE, RUNNING
from threading import Semaphore, Lock
from .ThreadObject import Thread
import os

def work_func(thread_pool):
    work_queue = thread_pool.tasks_queue
    while True:
        with thread_pool.cancle_lock:
            if thread_pool.cancle:
                return
        task = work_queue.get()
        if task is None:
            return
        try:
            # f = task.result
            task.result.set_status(RUNNING)
            # print(RUNNING)
            # print(task.result)
            # print(f'before{task}')
            value = task.target(*task.args, **task.kwargs)
            task.result.set_result(value)
            # print(f'after{task}')
            #
            # print(task.result)
        except Exception as e:
            # print(e)
            task.result.set_exception(e)

class ThreadPool:

    def __init__(self, maxworkers=None):

        if maxworkers is None:
            maxworkers = os.cpu_count()
        self._maxworkers = maxworkers
        self.tasks_queue = Queue()
        self.sem = Semaphore(0)
        self._threads = set()
        self._shut_down_lock = Lock()
        self._shut_down = False
        self.cancle = False
        self.cancle_lock = Lock()


    def submit(self, *, target=None, args=None, kwargs=None):
        with self._shut_down_lock:
            if self._shut_down:
                raise RuntimeError('can\'t submit task after this pool has been shutdown\n')
        f = future()
        task = item(target=target, args=args, kwargs=kwargs, result=f)
        self.tasks_queue.put(task)

        if not self.sem.acquire(blocking=False):
            if len(self._threads) < self._maxworkers:
                t = Thread(target=work_func, args=(self,))
                t.start()
                self._threads.add(t)
        return f

    def map(self, fn, *arglist):
        fs = [self.submit(target=fn, args=args) for args in zip(*arglist)]

        # 注意返回生成器的手法
        iterator = iter(fs)
        def generator():
            while True:
                try:
                    yield next(iterator).get_result()
                except Exception:
                    break
        return generator()

    def shutdown(self, *, cancle=False):
        with self._shut_down_lock:
            self._shut_down = True

        if cancle:
            with self.cancle_lock:
                self.cancle = True
            while True:
                try:
                    task = self.tasks_queue.get(block=False)
                    task.result.set_status(CANCLE)
                except Empty:
                    break
        else:
            threads_num = len(self._threads)
            for i in range(threads_num):
                self.tasks_queue.put(None)

        for t in self._threads:
            t.join()


    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_tracebace):
        # wait for all threads in this threadPool exit
        self.shutdown(cancle=False)
        return False