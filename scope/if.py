# python 中 if/for 的作用域不同于其他语言，在外部也是可以访问的。

# if 作用域
if True:
    obj = object()

print(obj)


# for 作用域
for i in range(2):
    pass

print(i)


# try/except 作用域
try:
    r = object()
    raise Exception()
except:
    e = object()
    pass

print(r)
print(e)

# while 作用域
while i < 2:
    w = object()
    i += 1

print(w)