#  __________________________
# / \                        \
#|   |                        |
# \_/| ----------||---------- |
#    |                        |
#    |        Code by:        |
#    |   Élie-David langlois  |
#    |                        |
#    |        RankItem        |
#    |                        |
#    |        Project:        |
#    |      PokemonPicker     |
#    |                        |
#    |        Created:        |
#    |      Su 2026-09-13     |
#    |      Version: 0.1      |
#    |                        |
#    |      Last update:      |
#    |      Su 2026-09-13     |
#    |      Version: 0.2      |
#    |                        |
#    | ----------||---------- |
#    |   _____________________|___
#    |  /                        /
#    \_/________________________/

from typing import cast, Any

type JSONValue = (int | float | bool | str | None
                  | list[JSONValue] | dict[str, JSONValue])


class Ranking[T]:
    type _FaceOffResult = tuple[list[Rankable[T]], list[Rankable[T]]]
    
    def __init__(self) -> None:
        self.ranking: list[Rankable[T]] = []
        self.history: list[Ranking._FaceOffResult] = []
    # --- End of function --- #
# --- End of class Ranking --- #





class RankingSession:
    def __init__(self) -> None:
        pass
    # --- End of function --- #
# --- End of class RankingSession --- #





class Rankable[T]:
    def __init__(self, obj: T) -> None:
        self.obj: T = obj
        self.name: str = getattr(self.obj, "name", str(self.obj))
        self.rank: int = 0
        self.lessers: list[Rankable[T]] = []
        self.betters: list[Rankable[T]] = []
    # --- End of function --- #





    def toDict(self) -> dict[str, JSONValue]:
        poke_dict: dict[str, JSONValue] = {}
        for key, val in vars(self).items():
            if isinstance(val, list):
                poke_dict[key] = Rankable._listToJSONList(cast(list[Any], val))
            elif isinstance(val, dict):
                poke_dict[key] = Rankable._dictToJSONDict(
                    cast(dict[str, Any], val))
            else : poke_dict[key] = val
        return poke_dict
    # --- End of function --- #





    @classmethod
    def _hasOnlySimpleAttributes(cls, obj: T) -> bool:
        return all(isinstance(attr, (str, int, float, bool, type(None)))
                   for attr in vars(obj).values())
    # --- End of function --- #





    @classmethod
    def _dictToJSONDict(cls, d: dict[str, Any]) -> dict[str, JSONValue]:
        return {key : (val.name if isinstance(val, Rankable) else val)
                for key, val in d.items()}
    # --- End of function --- #





    @classmethod
    def _listToJSONList(cls, l: list[Any]) -> list[JSONValue]:
        return [(elem.name if isinstance(elem, Rankable) else elem)
                for elem in l]
    # --- End of function --- #
# --- End of class RankItem --- #