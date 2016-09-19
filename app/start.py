from heroes.hero_builder import HumanHero, ElfHero, DwarfHero
from gameplay.fighting import battle

dwarfhero = DwarfHero(name="Gimli")
elfhero = ElfHero(name="Legolas")
humanhero = HumanHero(name="Dirk")

battle([humanhero, elfhero])
