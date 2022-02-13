# 可以 pickle 的类型
# 1. None、True、False
# 2. 整数、浮点数、复数
# 3. str、bytes
# 4. 只包含可 pickle 的容器对象(tuple、list、dict)
# 5. 模块顶层函数、自定以函数. pickle 传递的是module.func
# 6. 类. pickle 传递的是 module.class
# 7. 类实例，这些类的__dict__ 或者 __getstate__ 返回值可以 pickle, pickle 的是 module.class 和 dict 或者 __getstate__返回值

# 我们要明白为什么有这样的限制，就需要理解 unpickle 的时候，是如何解析的？
# 涉及到一个很关键的函数find_class，该函数是通过解释器目前加载的 sys.modules 来寻找类或者函数的，
# 所以只有模块顶层的成员才可以被 unpickle。

# def find_class(self, module, name):
#     # Subclasses may override this.
#     sys.audit('pickle.find_class', module, name)
#     if self.proto < 3 and self.fix_imports:
#         if (module, name) in _compat_pickle.NAME_MAPPING:
#             module, name = _compat_pickle.NAME_MAPPING[(module, name)]
#         elif module in _compat_pickle.IMPORT_MAPPING:
#             module = _compat_pickle.IMPORT_MAPPING[module]
#     __import__(module, level = 0)
#     if self.proto >= 4:
#         return _getattribute(sys.modules[module], name)[0]
#     else:
#         return getattr(sys.modules[module], name)

# def _getattribute(obj, name):
#     for subpath in name.split('.'):
#         if subpath == '<locals>':
#             raise AttributeError("Can't get local attribute {!r} on {!r}"
#                                  .format(name, obj))
#         try:
#             parent = obj
#             obj = getattr(obj, subpath)
#         except AttributeError:
#             raise AttributeError("Can't get attribute {!r} on {!r}"
#                                  .format(name, obj)) from None
#     return obj, parent


import pickle

class test_pickle:
    def __init__(self, i):
        self.i = i
    def inner_func(self):
        print(f"{self.i}")

def outter():
    def inner():
        print("call inner")
        return
    return inner

# 似乎对类内部函数甚至是绑定函数也可以pickle
def call():
    try:
        b = pickle.dumps(test_pickle(1).inner_func) # 传递对象、'inner_func'、getattr函数实现的
        # b = pickle.dumps(outter())
        print(b)
        func = pickle.loads(b)
        func()
    except Exception as e:
        print(f"when pickle class func, error happend: {e}")

if __name__ == '__main__':
    call()