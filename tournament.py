from ex2.strategy import BattleStrategy, NormalStrategy
from ex2.strategy import AggressiveStrategy, DefensiveStrategy
from ex2.strategy import StrategyError
from ex0.factory import CreatureFactory, FlameFactory, AquaFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    if len(opponents) < 2:
        print("Not enought creature")
        return
    lst = [f"({factory.create_base().name}+" +
           f"{strategy.__class__.__name__.replace('Strategy', '')})"
           for factory, strategy in opponents]
    print("[ " + ", ".join(lst) + " ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    for i in range(len(opponents) - 1):
        for j in range(i + 1, len(opponents)):
            print("* Battle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                print(strategy1.act(creature1))
            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            try:
                print(strategy2.act(creature2))
            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            if i != len(opponents) - 2:
                print()


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    battle(
            [
                (FlameFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())
            ]
    )
    print()
    print("Tournament 1 (error)")
    battle(
            [
                (FlameFactory(), AggressiveStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())
            ]

    )
    print()
    print("Tournament 2 (multiple)")
    battle(
            [
                (AquaFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy()),
                (TransformCreatureFactory(), AggressiveStrategy())
            ]

    )
