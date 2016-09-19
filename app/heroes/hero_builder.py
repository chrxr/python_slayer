class BaseHero:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.weapon_skill = 4
        self.ballistic_skill = 4
        self.hit_points = 4
        self.strength = 4
        self.toughness = 4
        self.armour = 0
        self.initiative = 2
        self.attacks = 1

    def hero_name(self):
        print(self.name)

    def hero_stats(self):
        for key, value in vars(self).items():
            text = str.format("{0} : {1}", key, value)
            print(text)

    def __str__(self):
        str_string = str.format("{0} the {1}", self.name, self.race)
        return str_string

    def __repr__(self):
        repr_string = str.format("{0}(name='{1}')", type(self).__name__, self.name)
        return repr_string

class HumanHero(BaseHero):
    def __init__(self,name):
        race = 'human'
        super(HumanHero, self).__init__(name,race)
        self.race = race
        self.armour = 2

class DwarfHero(BaseHero):
    def __init__(self, name):
        race = 'dwarf'
        super(DwarfHero, self).__init__(name, race)
        self.race = race
        self.ballistic_skill = 2
        self.toughness = 5
        self.armour = 3
        self.initiative = 1
        self.strength = 5

class ElfHero(BaseHero):
    def __init__(self, name):
        race = 'elf'
        super(ElfHero, self).__init__(name, race)
        self.race = race
        self.ballistic_skill = 6
        self.armour = 1
        self.weapon_skill = 5
        self.initiative = 3
