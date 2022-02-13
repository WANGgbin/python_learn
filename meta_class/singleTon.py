#介绍单例的几种实现模式
from threading import Lock
# 通过元类实现
# class SingleTon(type):
#     def __init__(cls, clsname, bases, attr):
#         super().__init__(clsname, bases, attr)
#         cls._instance = None
#         cls._lock = Lock()
#
#     def __call__(cls, *args, **kwargs):
#         if cls._instance is None:
#             with cls._lock:
#                 if cls._instance is None:
#                     cls._instance = super().__call__(*args, **kwargs)
#         return cls._instance
#
#
# class a(metaclass=SingleTon):
#     def __init__(self):
#         print("call a::__init__")

# 通过函数装饰器实现
from functools import reduce
from collections import OrderedDict
def SingleTon(cls):
    _instances = {}
    _lock = Lock()
    def wrapper(*args, **kwargs):
        key = cls.__name__ + '|'
        if args:
            key += reduce(lambda x, y: f"{x}|{y}", args)
        if kwargs:
            key += reduce(lambda x, y: f"{x}|{y}", OrderedDict(kwargs).items())
        print(key)
        if key not in _instances:
            with _lock:
                if key not in _instances:
                    _instances[key] = cls(*args, **kwargs)
        return _instances[key]

    return wrapper

@SingleTon
class b:
    def __init__(self, *,  a, b):
        self._a = a
        self._b = b
        print("call b::__init__")

if __name__ == '__main__':
    b(a=1, b=2)
    b(b=2, a=1)
    b(a=2, b=3)