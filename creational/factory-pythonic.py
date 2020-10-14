class ElfRider:
    pass

class Wizard:
    pass

class Knight:
    pass


class UnitFactory:
    units_dict = {
        'elfrider': ElfRider,
        'wizard': Wizard,
        'knight': Knight
    }

    @classmethod
    def create_unit(cls, unit_type):
        key = unit_type.lower()
        return cls.units_dict.get(key)()


class Kingdom:
    factory = UnitFactory

    def recruit(self, unit_type):
        unit = type(self).factory.create_unit(unit_type)
        print(type(self))
        self.pay_gold(unit)
        self.update_records(unit)
        return unit
        # type(self) == Kingdom.factory

    def pay_gold(self, something):
        print("Gold paid")

    def update_records(self, something):
        print ("Some logic")


if __name__ == '__main__':
    k = Kingdom()
    elf_unit = k.recruit('ElfRider')
    elf_unit.test()
    print(elf_unit)