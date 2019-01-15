from abc import ABCMeta, abstractmethod

class Enemy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def attack_player(self, player):
        pass


class EnvironmentAsset(object):
     __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self.mobile = False

# trap inherits from both enemy and environment class
class Trap(Enemy, EnvironmentAsset):
#     override the previous functions we created in the abstract classes
# we do the contructor: and initialise both base classes
    def __init__(self):
        super().__init__() # super refers to the parent class
        print("trap class")
        # if we want the base class to be called first we use super

    def attack_player(self, player):
        return player.health - 10



mine = Trap()
yours = Trap()