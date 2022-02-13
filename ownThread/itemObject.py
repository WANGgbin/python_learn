from .futureObject import future

class item:
    def __init__(self, *, target=None, args=None, kwargs=None, result=None):
        self.target = target
        self.args = args if args is not None else ()
        self.kwargs = kwargs if kwargs is not None else {}
        self.result = result if result is not None else future()


    def __repr__(self):
        return f'target:{self.target}\n' + f'args:{self.args}\n' + f'kwargs:{self.kwargs}\n' + f'result:{self.result}\n'


