from threading import Lock, Condition
_PENDING = 1
CANCLE = 2
RUNNING = 3
_FINISHED = 4

class CancelledError(Exception):
    pass

class future:
    def __init__(self):
        self.result = None
        self.exception = None
        self.status = _PENDING
        self._cond = Condition(Lock())

    def __repr__(self):
        return f'result:{self.result}\n' + f'exception: {self.exception}\n' + f'status: {self.status}'

    def set_result(self, value):
        with self._cond:
            print(self.status)
            if self.status in [_PENDING, CANCLE, _FINISHED]:
                raise RuntimeError('future has\'t been handle or cancled or finished\n')
            else:
                self.status = _FINISHED
                self.result = value
                self._cond.notify()

    def set_exception(self, e):
        with self._cond:
            if self.status in [_PENDING, CANCLE, _FINISHED]:
                raise RuntimeError('future has\'t been handle or cancled or finished\n')
            else:
                self.status = _FINISHED
                self.result = e
                self._cond.notify()

    def _get_result(self):
        if self.exception is not None:
            raise self.exception
        return self.result

    def get_result(self):
        with self._cond:
            if self.status is CANCLE:
                raise CancelledError()
            elif self.status is _FINISHED:
                return self._get_result()

            self._cond.wait()

            if self.status is CANCLE:
                raise CancelledError()
            elif self.status is _FINISHED:
                return self._get_result()

    def set_status(self, status):
        if status not in [CANCLE, RUNNING]:
            RuntimeError('only CANCLE is vanlid')
        with self._cond:
            self.status = status
            if status is CANCLE:
                self._cond.notify()


    def get_status(self):
        with self._cond:
            return self.status

            
        
        
        