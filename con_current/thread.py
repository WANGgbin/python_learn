# from threading import Thread
# Usage:
# 1、创建一个线程
# t = Thread(target=func, args=(), kwargs=(), daemon=True/False)
# a. 我们看看Thread对象最重要的成员：
#         if kwargs is None:
#             kwargs = {}
#         self._target = target  # 待执行对象
#         self._name = str(name or _newname())
#         self._args = args  # 位置参数
#         self._kwargs = kwargs  # 关键字参数
#         if daemon is not None:
#             self._daemonic = daemon
#         else:
#             self._daemonic = current_thread().daemon  # 如果未设置，则跟随当前线程的daemon属性
#         self._ident = None  # 维护一个全局的map，key:ident, val: thread(),函数current_thread就是通过此全局变量实现

#         self._tstate_lock = None  # 线程运行前初始化并占据次锁，当线程结束的时候，c代码会释放该锁，而join本质就是尝试占有此锁
#         self._started = Event()  # 线程开始运行前设置此成员
#
# b. daemon
# i. daemon -> False: 主线程执行完毕，会等待所有线程执行完毕才退出解释器。
# 所有非daemon綫程的tstate_lock锁会被扔到全局集合_shutdown_locks中，主线程执行完毕后执行函数_shutdown,
# 该函数会尝试占有所有的tstate_lock锁即等待所有的非daemon锁执行完毕。
# 详情参考threading._shutdown()
# # Join all non-deamon threads
#     while True:
#         with _shutdown_locks_lock:
#             locks = list(_shutdown_locks)
#             _shutdown_locks.clear()
#
#         if not locks:
#             break
#
#         for lock in locks:
#             # mimick Thread.join()
#             lock.acquire()
#             lock.release()
#
#         # new threads can be spawned while we were waiting for the other
        # threads to complete

# ii. daemon -> True: 当主线程执行完毕时，跟随主线程一起退出。
#
# 2、启动一个线程
# t.start()  # 实现原理：self._started
# 3、等待线程执行完毕
# t.join()  # 实现原理: self._tstate_lock
# 4、改变线程行为
# 改变线程行为有两种方式，一种是传递target，第二种是覆写run()函数(参考threading.Timer实现)。

from threading import Thread
