from weakref import ref, finalize
class a:
    pass

# finalizer 相对于 ref 优势在于用户无须关心弱引用对象的生命期，finalizer 创建的弱引用对象存在于finalizer的类属性dict中，从而保证了弱引用
# 对象生命期为全局。
def test_finalizer():
    obj = a()
    finalize(obj, lambda: print(" obj is released"))

if __name__ == '__main__':
    test_finalizer()

# finalizer对象是可调用的，实现了__call__方法。该方法本质就是将 finalizer 对象从finalizer类属性dict中 pop 然后执行注册的函数。
# 当用户主动调用后，obj gc的时候，不再调用回调函数，因为弱引用对象不再存在。
def test1_finalizer():
    obj = a()
    f = finalize(obj, lambda: print(" obj is released"))
    # 主动调用后，对象释放不再调用回调函数
    f()
    print('----------------')

if __name__ == '__main__':
    test1_finalizer()


# finalizer 注册了atexit函数，函数会调用所有属性atexit 为true的finalizer对象注册的函数。
# alive 判断finalizer对象是否存活，本质上就是判断finalizer object 是否在类属性dict中。

if __name__ == '__main__':
    obj = a()
    f = finalize(obj, lambda: print("obj is released"))

if __name__ == '__main__':
    obj = a()
    f = finalize(obj, lambda: print("obj is released"))
    f.atexit = False # 回调不会被执行