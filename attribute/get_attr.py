# 主要验证 属性访问的先后顺序
# getter -> instance attr -> cls attr

class getter:
    def __get__(self, instance, cls):
        return "getter"

class getter_and_setter:
    str = "getter_and_setter"
    def __get__(self, instance, cls):
        return  getter_and_setter.str

    def __set__(self, instance, val):
        getter_and_setter.str = val


class c:
    g = getter()
    g_and_s = getter_and_setter()
    _attr = None
    def __init__(self):
        # 属性设置，如果getter_and_setter 和 instance 不存在属性，则添加属性到实例中
        self.g = "instance: g"
        self.g_and_s = "instance: g_and_s"


class d:
    def __init__(self, obj):
        if not isinstance(obj, dict):
            raise TypeError("par must be a dict instance")
        self.obj = obj

    # __getattr__ 委托不了双下划线开头和结尾的方法， 需要手动委派
    def __getattr__(self, attr):
        print(attr)
        return getattr(self.obj, attr)

    # def __getitem__(self, key):
    #     return self.obj[key]

if __name__ == '__main__':
    obj = c()
    print(getattr(obj, "g"))
    print(getattr(obj, "g_and_s"))
    print(getattr(c, "g_and_s"))
    # obj = d({"key": "val"})
    # print(obj.__getitem__("key"))