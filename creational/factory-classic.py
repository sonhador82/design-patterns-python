# легко создавать разные объекты


class UnitFactory:
    def create_unit(self, unit_type):
        unit = None

        if unit_type == 'ElfRider':
            unit = ElfRider()
        elif unit_type == 'Knight':
            unit = Knight()
        elif unit_type == 'Wizard':
            unit = Wizard()
        return unit

class ElfRider:
    pass

class Wizard:
    pass

class Knight:
    pass

class Kingdom:
    def __init__(self, factory: UnitFactory):
        self.factory = factory

    def recruit(self, unit_type):
        unit = self.factory.create_unit(unit_type)
        self.pay_gold(unit)
        self.update_records(unit)
        return unit

    def pay_gold(self, something):
        print("Gold paid")

    def update_records(self, something):
        print("Some logic to update")

if __name__ == '__main__':
    factory = UnitFactory()
    k = Kingdom(factory)
    elf_unit = k.recruit('ElfRider')
    print(elf_unit)

