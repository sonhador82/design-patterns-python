# паттерн стратегия - инкапсулировать и менять алгоритм в рантайме

from abc import ABCMeta, abstractmethod


class AbstractGameUnit(metaclass=ABCMeta):
    def __init__(self, name, jump_object=None):
        self.jump_strategy = None
        self.name = name
        self.set_jump_strategy(jump_object)

    def set_jump_strategy(self, jump_object=None):
        """ установить объект стратегию (алгоритм)"""
        if isinstance(jump_object, JumpStrategy):
            self.jump_strategy = jump_object
        else:
            self.jump_strategy = JumpStrategy()

    def jump(self):
        try:
            self.jump_strategy.jump()
        except AttributeError as e:
            print("Error: AbstractGameUnit.jump: ", e.args)

    @abstractmethod
    def info(self):
        pass

# strategies
class JumpStrategy:
    def jump(self):
        print("JumpStrategy: Default")


class PowerJump(JumpStrategy):
    def jump(self):
        print("JumpStrategy: Power Jump")


class HorseJump(JumpStrategy):
    def jump(self):
        print("JumpStrategy: HorseJump")


# units
class DwarfFighter(AbstractGameUnit):
    def info(self):
        print("I am great dwarf")


if __name__ == '__main__':
    jump_strategy = PowerJump()
    dwarf = DwarfFighter("Dwarf", jump_strategy)
    print("Strategy try to jump")
    dwarf.jump()

    print("Change strategy later")
    dwarf.set_jump_strategy(HorseJump())
    dwarf.jump()
