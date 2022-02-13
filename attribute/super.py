# super() 既可以作用于 classmethod 也可以作用于实例方法
class a:
    @classmethod
    def get_cls_name(cls):
        print(cls)
        return cls.__name__

class b(a):
    @classmethod
    def get_cls_name(cls):
        return super().get_cls_name()


if __name__ == '__main__':
    print(b().get_cls_name())