# в пайтоне функции first class objects

from abc import ABCMeta, abstractmethod
from collections.abc import Callable


class AbstractGameUnit(metaclass=ABCMeta):
    def __init__(self, name, jump_strategy):
        assert(isinstance(jump_strategy, Callable))
        self.name = name
        self.jump = jump_strategy

    @abstractmethod
    def info(self):
        pass


class DwarfFighter(AbstractGameUnit):
    def info(self):
        print("I am a great dwarf")

# strategies
def power_jump():
    print("Powerjump: jump")


def horse_jump():
    print("Horse jump: jump")


if __name__ == "__main__":
    dwarf = DwarfFighter("Dwarf", power_jump)
    print("Strategy Power jump")
    dwarf.jump()

    # change in runtime
    dwarf.jump = horse_jump
    dwarf.jump()
