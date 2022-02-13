import importlib
from sys import modules

print('func_tools' in modules)

# 用来导入一个 module
importlib.import_module('func_tools')

# 还可以使用 __import__， 但是不建议使用
print('func_tools' in modules)
