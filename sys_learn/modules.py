# python sys.modules 用于存储解释器目前为止所有import的module，是一个dict结构
# key 为 module 名，module 是全局唯一的，value 是 module 对象。module 的 _dict__
# 中存放了当前 module 中所有的 symbol，包括 func、class、module、var，key 是 符号名，
# val 是特定的对象。

# 从其他 module 中导入的 symbol 当然也会记录在当前 moudle 的 __dict__ 中，key 同样是
# symbol 名，val 是导入 module 中定义的对象。
# 如果导入的是一个 module，当前 module 的 __dict__ 中就会记录一个 module 对象。

