from ex0 import CreatureFactory, FlameFactory, AquaFactory


def testing_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def testing_base_fight(
    factory_1: CreatureFactory, factory_2: CreatureFactory
) -> None:
    print("Testing battle")
    base_creature_1 = factory_1.create_base()
    base_creature_2 = factory_2.create_base()
    print(base_creature_1.describe())
    print("vs.")
    print(base_creature_2.describe())
    print("fight!")
    print(base_creature_1.attack())
    print(base_creature_2.attack())


if __name__ == "__main__":
    testing_factory(FlameFactory())
    print()
    testing_factory(AquaFactory())
    print()
    testing_base_fight(FlameFactory(), AquaFactory())
