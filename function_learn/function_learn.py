# python 内部的函数也是对象，是类 <class 'function'> 的实例。
# function 定义了 __get__ 方法，该方法可以将函数对象绑定到一个实例或者类上。
# getattr(instance, func) 或者 func.__get__(instance) 都可以对函数进行绑定


def func(self):
    print(self)

class test:
    def inner(self):
        print(self)

if __name__ == '__main__':
    print(type(func))
    func.__get__(1, None)()

    print(type(test.inner))
    test.inner.__get__(1, None)()
    print(func.__class__.__dict__)
    print('-' * 8)
    print(test.__dict__)