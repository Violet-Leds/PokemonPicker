#  __________________________
# / \                        \
#|   |                        |
# \_/| ----------||---------- |
#    |                        |
#    |        Code by:        |
#    |   Élie-David langlois  |
#    |                        |
#    |      PokemonPicker     |
#    |                        |
#    |        Created:        |
#    |       2025-11-14       |
#    |      Version: 0.1      |
#    |                        |
#    |      Last update:      |
#    |       2025-11-14       |
#    |      Version: 0.1      |
#    |                        |
#    | ----------||---------- |
#    |   _____________________|___
#    |  /                        /
#    \_/________________________/



from time import time
from Python_Utils.Templates.ProgramLoop2 import programLoop
t1: float = time()
head_l: int = 40

import random



def main() -> None:
    names: list[str] = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", 
                        "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie"]
    
    pokemons: list[Pokemon] = [Pokemon(i, names[i - 1]) for i in range(1, 11)]

    nextRound: list[int] = [pokemon.pokeId-1 for pokemon in pokemons]
    rankedList: list[int] = []

    thisRound: list[int] = nextRound[:]
    eleminated: list[int] = []

    while(len(nextRound)):
        if len(nextRound) == 1:
            print(eleminated, nextRound) # debug
            i: int = 0
            while i < len(eleminated):
            # for i in range(len(eleminated)):
                print(i, len(eleminated), "yo") # debug
                if nextRound[0] == pokemons[eleminated[i]].worstThan:
                    nextRound.append(eleminated.pop(i))
                    i -= 1
                    print(nextRound, i) # debug
                i += 1

            rankedList.append(nextRound.pop(0))
            print(f"\n{pokemons[rankedList[-1]].name} has been added to the ranking.\n")
            print(nextRound) # debug
        else:
            thisRound = nextRound[:]
            random.shuffle(thisRound)
            nextRound = []

            while(len(thisRound) > 1):
                print("\n", thisRound[0], thisRound[1]) # debug
                answer: str = ""
                while(not answer in ["0", "1"]):
                    query: str = (
                        "Which do you prefer?"
                        f"\n{pokemons[thisRound[0]].name} (0) or "
                        f"{pokemons[thisRound[1]].name} (1)"
                        "\nEnter the number of you choice and press 'Enter': "
                    )
                    answer = input(query)
                winner: int = int(answer)
                
                pokemons[thisRound[winner]].betterThan.append(thisRound[1 - winner])
                pokemons[thisRound[1 - winner]].worstThan = thisRound[winner]
                nextRound.append(thisRound.pop(winner))
                eleminated.append(thisRound.pop(0))
        
            if thisRound: nextRound.append(thisRound.pop())

# --- End of function --- #





class Pokemon:
    pokeId: int = -1
    name: str = ""
    betterThan: list[int] = []
    worstThan: int = -1

    def __init__(self, pokeId: int, name: str) -> None:
        self.pokeId = pokeId
        self.name = name

    def defeatedBy(self, pokeId: int) -> None:
        self.worstThan = pokeId

    def hasDefeated(self, pokeId: int) -> None:
        self.betterThan.append(pokeId)

# --- End of class --- #





if __name__ == "__main__": programLoop(main, t1, head_l)