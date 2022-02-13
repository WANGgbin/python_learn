from threading import Lock
from threading import Thread
from enum import Enum
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
# By redefinite meta class's func __call__ , we can specify the instance creation.
class SingleTon(type):
    def __init__(cls, name, bases, dict):
        super().__init__(name, bases, dict)
        cls._instance = None
        cls.lock = Lock()
        print(dict)
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls.lock.acquire()
            if cls._instance is None:
                cls._instance = super().__call__(*args, **kwargs)
            cls.lock.release()
        return cls._instance

class client:
    def __init__(self, psm):
        pass
class rpcBase(metaclass=SingleTon):
    pass

class rpc(rpcBase):
    def __new__(cls, psm):
        print('call rpc::__new__')
        return super().__new__(cls)

    def __init__(self, psm):
        self.client = client(psm)

def thread_exec():
    for i in range(100000):
        obj = rpc("a.b.c")

class myEnumMeta(type):
    def __new__(metaclass, cls, bases, dictionary):
        cls_obj = super().__new__(metaclass, cls, bases, dictionary)
        cls_obj._value_to_member = {}
        for key, value in dictionary.items():
            if key.startswith('_'):
                continue
            instance = cls_obj(value)
            print(key)
            setattr(cls_obj, key, instance)
            cls_obj._value_to_member[value] = instance
        return cls_obj

class myEnumBase(metaclass=myEnumMeta):
    def __new__(cls, value):
        if value not in cls._value_to_member:
            instance = super().__new__(cls)
            setattr(instance, 'value', value)
            return instance
        return cls._value_to_member[value]
    def __init__(self, value):
        print('__init__')

class myEnum(myEnumBase):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 2

class person:
    country = 'China'
    def __init__(self, name):
        self.name = name

    @classmethod
    def clsmethod(cls, name):
        print(f'cls: {cls}, name: {name}')

class son(person):
    def call_clsmethod(self):
        super().clsmethod('w')

from collections import OrderedDict
from functools import partial
from threading import local
def func(*args, arg1=0):
    print(*args, arg1)

class test:
    # __slots__ = ['i', 'j']
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def __hash__(self):
        return self.i + self.j
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j


from weakref import ref, WeakKeyDictionary, getweakrefcount, getweakrefs, finalize
import sys
import atexit
def func1(_, name='wgb'):
    print(_)

def printInfo():
    items = list(test_weak_key_dict.items())
    print(len(items))
    for k, v in test_weak_key_dict.items():
        print(k, v)
    print(test_weak_key_dict.keyrefs())

atexit.register(printInfo)

def call_back(name=''):
    time.sleep(0.5)
    print(f'call_back: {name}')

# obj = test(1, 2)
# wref = finalize(obj, call_back)
obj_weak_ref = WeakKeyDictionary()

class test_weakref:
    def __init__(self):
        self.objs = []
        # finalize(self.objs,  call_back, 'self.objs')
        for i in range(5):
            obj = test(i, i + 1)
            finalize(obj, call_back, f'obj: {i}')
            self.objs.append(obj)
            obj_weak_ref[obj] = i

test_weak_key_dict = WeakKeyDictionary()
w_ref = None


def tmp():
    obj = test(1, 2)
    print(obj)
    test_weak_key_dict[obj] = 1
    finalize(obj, call_back, 'obj')

class default_par:
    def __init__(self):
        self.members = [1, 2, 3]
    def get_func(self):
        def func(arg1, arg2=self.members):
            print(arg1)
            print(arg2)
        return func
import time
from threading import current_thread
from math import sqrt
def concurrent_calculate_type(limit=0, worker_num=0):
    def work(start, end):
        sum = 0
        for i in range(end - start):
            tmp = start + i
            sum += sqrt(tmp)
        # print(f'current_thread:{current_thread()}: sum: {sum}')

    begin = time.time()
    workers = []
    part = limit // worker_num
    for i in range(worker_num):
        t = Thread(target=work, args=(part * i, part * (i + 1),), daemon=False)
        workers.append(t)

    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print(f'limit: {limit}, worker_num: {worker_num} cost: {time.time() - begin} seconds')

def concurrent_io_type(limit=0, task_num=0, worker_num=0):
    def work(limit=limit, times=0):
        for i in range(times):
            sum = 0
            for i in range(limit):
                tmp = i
                sum += sqrt(tmp)
            time.sleep(6)
        # print(f'current_thread:{current_thread()}: sum: {sum}')

    begin = time.time()
    workers = []
    times = task_num // worker_num
    for i in range(worker_num):
        t = Thread(target=work, kwargs={'times': times}, daemon=False)
        workers.append(t)

    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print(f'limit: {limit}, worker_num: {worker_num} cost: {time.time() - begin} seconds')

class MyThreadPool(ThreadPoolExecutor):
    def __init__(self, maxsize, worker_num):
        super().__init__(max_workers=worker_num)
        self._work_queue = Queue(maxsize)
        self.lock = Lock()

    def submit(self, target, *args, **kwargs):
        with self.lock:
            if self._work_queue.full():
                print('work_queue is full, drop data')
                return
            super().submit(target, *args, **kwargs)

def func_thread():
    pool = MyThreadPool(4, 3)
    for i in range(10):
        pool.submit(target=call_back, name=f'{i}')
    return pool._threads

class pro:
    @property
    def name(self):
        return self._name

class delegate:
    def __init__(self):
        self.i = 1
    def __getattr__(self, attr):
        print(f'Getattr::Attr: {attr} does not exists')
    def __getattribute__(self, attr):
        print(f'Getattribute::Attr {attr} attr does not exists')
        return super().__getattribute__(attr)

import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        print(cls)
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

def output(self):
    print(f'{self.year}:{self.month}:{self.day}')
from abc import abstractmethod
class NewDate(Date):
    @classmethod
    @abstractmethod
    def today(cls):
        return super().today()
from functools import total_ordering
from types import MethodType

def args(default=False, *, debug=True, **kwargs):
    print(default)
    print(debug)
    print(kwargs)

def args1(arg1, *args, **kwargs):
    print(arg1)
    print(type(args))
    print(kwargs)

class meta(type):
    def print_info(cls):
        print("call meta::print_info")
        print(cls.__name__)

class a(metaclass=meta):
    pass
import os
from multiprocessing import Process

def run():
    pid = os.fork()
    if pid == 0:
        print(pid)
        print(id(pid))
        exit(0)
    else:
        print(pid)
        print(id(pid))
        print(os.waitpid(pid, 0))

class b:
    def funb(self):
        print("call b::funcb\n")

class wrapper:
    def __init__(self, b):
        self._b = b
    def __getattr__(self, func):
        attr = getattr(self._b, func)
        print(attr)
        return attr

def fun():
    pass
print(sys.modules['__mp_main__'].__dict__)

import pickle
from attribute import get_attr
m = {"key": 1, 2: None, 3: False}
class pick:
    def __init__(self):
        self.F = False
        self.t = True
        self.i = 1
        self.f = 1.01
        self.l = [1, 2]
import logging
if __name__ == '__main__':
    # o = object()
    # print(b.funb)
    # print(b.funb.__get__(o, None))
    # print(b.funb.__get__(None, object))
    # print(fun.__dict__)
    # print(pickle.dumps(fun))
    # print(pickle.dumps(wrapper, 1))
    # print(pickle.dumps(True))
    # print(pickle.dumps(False))
    # print(pickle.dumps(1.1, 1))
    # print(pickle.dumps(wrapper(True), 1))
    # print(wrapper(True).__dict__)
    # print(sys.modules['__mp_main__'].__dict__)
    # print(sys.modules.keys())
    # o = pick()
    # print(pickle.dumps(o))

    # logger = logging.getLogger('a')
    _ = 1
    a = _
    print(f'a: {a}')