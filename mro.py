from queue import *

class MRO:
    def __init__(self,obj):
        self.obj = obj

    def __getattr__(self, item):

        if self.check_if_item_in_obj(self.obj, item):
            return getattr(self.obj, item)

        self.q = Queue(maxsize=0)
        self.q.put(self.obj.__class__)

        while self.q.qsize() > 0 :
            j = self.q.get()
            self.add_queue(j)
            if self.check_if_item_in_obj(j,item) :
                if callable(getattr(j,item)):
                    def f(*args, **kwargs):
                        return getattr(j,item)(self.obj,*args,**kwargs)
                    return f
                else:
                    return getattr(j,item)

        return super(MRO,self).__getattr__(item)


    def add_queue(self,obj):
        for i in reversed( obj.__bases__ ) :
            if i != object:
                self.q.put(i)

    def check_if_item_in_obj(self, obj,item):
        for i in obj.__dict__:
            if i == item:
             return True
        return False

