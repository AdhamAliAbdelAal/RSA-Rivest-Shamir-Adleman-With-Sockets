import threading
class thread(threading.Thread):
    def __init__(self, target, args=()):
        threading.Thread.__init__(self)
        self.target = target
        self.args = args
    def run(self):
        try:
            self.target(*self.args)
        except Exception as e:
            self.exception = e
    def join(self):
        threading.Thread.join(self)
        if(self.exception):
            raise self.exception