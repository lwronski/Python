
def inst(cls):
    counter = 0

    class Counter_clas(cls):

        def __init__(self, *args, **kargs):
            super(Counter_clas,self).__init__(*args, **kargs)
            nonlocal counter
            counter += 1

        def numOfInst():
            nonlocal counter
            print("Liczba instancji klasy {0}: {1}".format( cls.__name__, counter))


    return Counter_clas
