import time, functools

def timer(func):
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        t = time.time()
        func()
        t2 = time.time()
        print(func.__name__ +  " %.2f secondi: "  % (t2-t))
    return _timer