#  __________________________
# / \                        \
#|   |                        |
# \_/| ----------||---------- |
#    |                        |
#    |        Code by:        |
#    |       Violet-Leds      |
#    |                        |
#    |         Ranking        |
#    |                        |
#    |        Project:        |
#    |      PokemonPicker     |
#    |                        |
#    |        Created:        |
#    |      Su 2026-09-13     |
#    |      Version: 0.2      |
#    |                        |
#    |      Last update:      |
#    |      We 2026-09-18     |
#    |     Version: 0.2.3     |
#    |                        |
#    | ----------||---------- |
#    |   _____________________|___
#    |  /                        /
#    \_/________________________/

from typing import cast, Any
from random import shuffle
import sys

type JSONValue = (int | float | bool | str | None
                  | list[JSONValue] | dict[str, JSONValue])
FACE_OFF_SIZE: int = 3
names: list[str] = ["Bulbasaur", "Ivysaur", "Venusaur",
                    "Charmander", "Charmeleon", "Charizard",
                    "Squirtle", "Wartortle", "Blastoise"]
    
class RankingSession[T]:
    """
    One ranking with one set of settings.
    """
    type _FaceOffResult = tuple[list[Rankable[T]], list[Rankable[T]]]
    type _Event = _FaceOffResult | str
    type _History = list[_Event]
    
    def __init__(self, contenders: list[T] = []) -> None:
        self.history: RankingSession[T]._History = []
        self.settings: dict[str, int] = {}
        self._setContendersFromSettings(contenders)
        self.unranked: list[Rankable[T]] = self.contenders[:]
        self.ranking: list[Rankable[T]] = []
        self.eliminated: list[Rankable[T]] = []
        self.this_round: list[Rankable[T]] = []
        self.next_round: list[Rankable[T]] = self.unranked[:]
    # --- End of function --- #





    def run(self) -> None:
        """
        Run the ranking session.
        """
        self.history.append("Session start")
        while self.unranked:
            self._oneRound()
            if len(self.next_round) == 1 : self._putNextFavoriteInRank()
        self.history.append("Session end")
        self._showRanking()
        self.printHistory()
    # --- End of function --- #





    def printHistory(self) -> None:
        print("\nHistory:")
        for line in self.history:
            if isinstance(line, str) : print(line)
            else : print(self._faceOffToString(line))
    # --- End of function --- #





    def _faceOffToString(self, face_off: _FaceOffResult) -> str:
        face_off_str: str = (
            "Face-off:\n"
            f"    Winners : {", ".join([w.name for w in face_off[0]])}\n"
            f"    Losers : {", ".join([l.name for l in face_off[1]])}"
        )
        return face_off_str
    # --- End of function --- #





    def _showRanking(self) -> None:
        print("Done! Here's the final ranking:")
        for i, ranked in enumerate(self.ranking):
            print(f"{i + 1}. {ranked.name}")
    # --- End of function --- #





    def _putNextFavoriteInRank(self) -> None:
        next_favorite: Rankable[T] = self.next_round.pop()
        self.history.append(f"{next_favorite.name} added to ranking")
        self.unranked.remove(next_favorite)
        self.ranking.append(next_favorite)

        print(f"--- {next_favorite.name}"
              " has been added to the ranking! ---") ### debug ###
        
        self._bringBackEliminated(next_favorite)
        input() ### debug ###
    # --- End of function --- #





    def _bringBackEliminated(self, next_favorite: Rankable[T]) -> None:
        print("Bringing back those defeated by "
                      f"{next_favorite.name}") ### debug ###

        for lesser in next_favorite.lessers:
            if self._allBettersAreRanked(lesser):
                self.eliminated.remove(lesser)
                self.next_round.append(lesser)
                print(lesser.name) ### debug ###

        self.history.append("Bringing back "
            f"{", ".join([contender.name for contender in self.next_round])}")
    # --- End of function --- #





    def _allBettersAreRanked(self, lesser: Rankable[T]) -> bool:
        return all(l in self.ranking for l in lesser.betters)
    # --- End of function --- #





    def _oneRound(self) -> None:
        """
        One round
        """
        print("\n- New Round -\n") ### debug ###
        self.history.append("New round")
        self._resetRound()
        print([cont.name for cont in self.this_round]) ### debug ###
                    
        while self.this_round:
            if len(self.this_round) == 1 : self._transferLastToNextRound()
            else : self.history.append(self._oneFaceOff())

        print([cont.name for cont in self.next_round]) ### debug ###
    # --- End of function --- #





    def _transferLastToNextRound(self) -> None:
        print(f"\nLast member of round {self.this_round[0].name}"
              " transfered to next round") ### debug ###
        self.history.append(f"{self.this_round[0].name}"
                            " transfered to next round")
        self.next_round.append(self.this_round.pop())
    # --- End of function --- #





    def _resetRound(self) -> None:
        self.this_round = self.next_round[:]
        self.next_round = []
        shuffle(self.this_round)
    # --- End of function --- #





    def _oneFaceOff(self) -> _FaceOffResult:
        """
        One face-off
        """
        print() ### debug ###
        face_off_contenders: list[Rankable[T]] = [
            self.this_round.pop() 
            for _ in range(min(FACE_OFF_SIZE, len(self.this_round)))]
        
        chosen_indicies: list[int] = self._compare(face_off_contenders)
        winners: list[Rankable[T]] = [
            face_off_contenders.pop(n) for n in chosen_indicies]
        
        Rankable[T].updateLessersBetters(face_off_contenders, winners)

        self.next_round += winners
        self.eliminated += face_off_contenders
        print(f"Winners : {[w.name for w in winners]}") ### debug ###
        print(f"Losers : {[l.name for l in face_off_contenders]}") ### debug ###
        print(f"Eliminated : {[e.name for e in self.eliminated]}") ### debug ###
        return (winners, face_off_contenders)
    # --- End of function --- #





    def _compare(self, face_off_contenders: list[Rankable[T]]) -> list[int]:
        """
        Prints conenders and asks answer.
        """
        for i, contender in enumerate(face_off_contenders):
            print(f"{i + 1}) {contender.name}")

        choice: str = input("Enter the numbers of your favorites"
                            " among these, separated by commas.\n"
                            ).replace(" ", "")

        chosen_indicies: list[int] = sorted(
            [int(n) - 1 for n in choice.split(",")], reverse=True)

        if chosen_indicies == []:
            chosen_indicies = list(range(len(face_off_contenders)))
        
        return chosen_indicies
    # --- End of function --- #





    def _setContendersFromSettings(self, contenders: list[T] = []) -> None:
        """
        Creates list of contenders from settings.
        """
        self.contenders: list[Rankable[T]] = [
            Rankable(contender) for contender in contenders]
    # --- End of function --- #
# --- End of class RankingSession --- #










class Rankable[T]:
    """
    One item to be ranked
    """
    def __init__(self, obj: T) -> None:
        self.obj: T = obj
        self.name: str = getattr(self.obj, "name", str(self.obj))
        self.rank: int = 0
        self.lessers: list[Rankable[T]] = []
        self.betters: list[Rankable[T]] = []
    # --- End of function --- #





    @classmethod
    def updateLessersBetters(cls, lessers: list[Rankable[T]],
                             betters: list[Rankable[T]]) -> None:
        for better in betters:
            common: list[str] = [l.name for l in lessers if l in better.lessers]
            if common:
                print(f"Error : {common} already in {better.name}'s lessers.")
                sys.exit()
            else : better.lessers += lessers
        for lesser in lessers:
            common = [l.name for l in betters if l in lesser.betters]
            if common:
                print(f"Error : {common} already in {lesser.name}'s betters.")
                sys.exit()
            else : lesser.betters += betters
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