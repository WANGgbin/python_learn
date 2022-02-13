# 介绍弱引用相关，某些场景下，为了避免内存的泄露(循环引用)，需要使用弱引用，保证对象可以被释放

from weakref import ref, finalize
import atexit

class a:
    pass


# if __name__ == '__main__':
#     obj = a()
#     wr = ref(obj)
#     print(obj is wr())
#     # finalize注册回调函数被调用，但是wr()仍然可以访问到变量，zh
#     # obj is released!
#     # <__main__.a object at 0x000001A8EEEE0FD0>
#
#     atexit.register(lambda: print(wr()))
#     finalize(obj, lambda: print("obj is released!"))
#
# # 这里仍然可以访问到 if block 中定义的变量
# print(obj)
# print(wr)
# print(wr())


def func():
    obj = a()
    wr = ref(obj)
    print(obj is wr())
    atexit.register(lambda: print(wr()))
    finalize(obj, lambda: print("obj is released!"))

if __name__ == '__main__':
    func()