from _thread import allocate_lock, start_new_thread, get_ident
from threading import Event, Lock

_global_map = {}
_global_lock = Lock()

class Thread:
    def __init__(self, *, target=None, args=(), kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._start = Event()
        self._finished_lock = allocate_lock()
        self._finished = False
        self._ident = None

    def start(self):
        self._create_new_thread()
        self._start.wait()

    def _create_new_thread(self):
        start_new_thread(self._run, ())

    def _run(self):
        self._ident = get_ident()
        with _global_lock:
            _global_map[self._ident] = self

        self._finished_lock.acquire()
        self._start.set()
        if self._target is not None:
            self._target(*self._args, **self._kwargs)
        self._finished_lock.release()
        with _global_lock:
            del _global_map[get_ident()]


    def join(self):
        self._finished_lock.acquire()
        self._finished = True

    def is_alive(self):
        if self._finished:
            return False
        if self._finished_lock.acquire(blocking=False):
            self._finished = True
            self._finished_lock.release()
            return False
        else:
            return True

    def get_id(self):
        return self._ident

def current_thread():
    with _global_lock:
        return _global_map[get_ident()]




