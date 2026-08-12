from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import TransformCapability, HealCapability
from typing import cast


class StrategyError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return creature.attack()
        raise StrategyError(f"Invalid Creature '{creature.name}'"
                            " for this normal strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, TransformCapability) and
                isinstance(creature, Creature))

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            transformer = cast(TransformCapability, creature)
            return "\n".join(
                [transformer.transform(),
                 creature.attack(),
                 transformer.revert()]
            )
        else:
            raise StrategyError(f"Invalid Creature '{creature.name}'"
                                " for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, HealCapability) and
                isinstance(creature, Creature))

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            healer = cast(HealCapability, creature)
            return "\n".join([creature.attack(), healer.heal()])
        else:
            raise StrategyError(f"Invalid Creature '{creature.name}'"
                                " for this defensive strategy")
