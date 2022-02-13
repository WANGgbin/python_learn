def callable(obj):
    return hasattr(obj, "__call__")

class partile:
    def __new__(cls, func, *args, **kwargs):
        if not callable(func):
            raise TypeError("func must be callable")
        self = super().__new__(cls)
        self._func = func
        self._args = args
        self._kwargs = kwargs
        return self

    def __call__(self, *args, **kwargs):
        all_kwargs = {**self._kwargs, **kwargs}
        return self._func(*self._args, *args, **all_kwargs)

def func(obj1, obj2):
    return obj1 + obj2

if __name__ == '__main__':
    print(partile(func, 1)(3))