from abc import ABCMeta, abstractmethod

class BaseClass(object):
    __metaclass__ = ABCMeta

    # decorator
    @abstractmethod
    def printHam(self):
        pass


class InClass(BaseClass):
    def printHam(self):
        print("HAM")


print("running this class")
x = InClass()
x.printHam()