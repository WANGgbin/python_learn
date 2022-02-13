# 模拟 staticmethod 装饰器，本质上通过描述符协议将函数从类的属性中剥离
class staticmethod:
    def __init__(self, func):
        self._func = func

    def __get__(self, instance, cls):
        return self._func

class TryStaticMethod:
    @staticmethod
    def get_class_name():
        return TryStaticMethod.__name__


if __name__ == '__main__':
    print(TryStaticMethod.get_class_name())
    print(TryStaticMethod().get_class_name())
