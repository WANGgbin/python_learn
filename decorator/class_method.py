from functools import partial
class classmethod:
    def __init__(self, func):
        self._func = func

    # def __get__(self, instance, cls):
    #     if instance is not None:
    #         raise TypeError("classmethod must be called only by cls")
    #     def wrapper(*args, **kwargs):
    #         self._func(cls, *args, **kwargs)
    #     return wrapper

    def __get__(self, instance, cls):
        if instance is not None:
            raise TypeError("classmethod must be called only by cls")
        return partial(self._func, cls)


class TryClassMethod:
    @classmethod
    def get_class_name(cls):
        print(cls.__name__)

if __name__ == "__main__":
    TryClassMethod.get_class_name()
    TryClassMethod().get_class_name()  # raise error

