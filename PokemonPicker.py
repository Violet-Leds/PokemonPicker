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
#    |       2025-11-26       |
#    |      Version: 0.2      |
#    |                        |
#    | ----------||---------- |
#    |   _____________________|___
#    |  /                        /
#    \_/________________________/



from time import time
from Python_Utils.Templates.ProgramLoop2 import programLoop
t1: float = time()
head_l: int = 50

import random


class Pokemon:
    
    
    def __init__(self, pokeId: int = -1, name: str = "Unknown") -> None:
        self.pokeId: int = pokeId
        self.name: str = name
        self.pokemons_it_has_defeated: list[Pokemon] = []
        self.pokemon_it_was_defeated_by: Pokemon | None = None

# --- End of class --- #





names: list[str] = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", 
                        "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie"]
    
pokemons: list[Pokemon] = [Pokemon(i, names[i - 1]) for i in range(1, 11)]



def main() -> None:
    not_compared_yet_this_round: list[Pokemon] = []
    eliminated: list[Pokemon] = []
    final_ranking: list[Pokemon] = []
    not_ranked: list[Pokemon] = [pokemon for pokemon in pokemons]
    qualifies_for_next_round: list[Pokemon] = not_ranked[:]
    random.shuffle(qualifies_for_next_round)

    # Loop iterating the rounds
    while not_ranked:
        print("\n- New Round -\n") # debug
        not_compared_yet_this_round = qualifies_for_next_round[:]
        qualifies_for_next_round = []
        oneRound(not_compared_yet_this_round, eliminated, qualifies_for_next_round)

        # When there's only one pokemon left
        if len(qualifies_for_next_round) == 1:
            next_favorite: Pokemon = qualifies_for_next_round.pop()
            print(f"\n--- {next_favorite.name} has been added to the ranking! ---\n")
            print(f"Bringing back those defeated by {next_favorite.name}")
            for loser in next_favorite.pokemons_it_has_defeated:
                eliminated.remove(loser)
                qualifies_for_next_round.append(loser)
                print(loser.name) # debug
                
            not_ranked.remove(next_favorite)
            final_ranking.append(next_favorite)

    print("\nDone! Here's the final ranking :")
    for i, pokemon in enumerate(final_ranking):
        print(f"{i + 1}. {pokemon.name}")

# --- End of function --- #





def oneRound(not_compared_yet_this_round: list[Pokemon],
             eliminated: list[Pokemon],
             qualifies_for_next_round: list[Pokemon]) -> None:
    while(len(not_compared_yet_this_round) > 1):
        contender1: Pokemon = not_compared_yet_this_round.pop()
        contender2: Pokemon = not_compared_yet_this_round.pop()
        winner: Pokemon
        loser: Pokemon
        winner, loser = compare(contender1, contender2)
        eliminated.append(loser)
        qualifies_for_next_round.append(winner)

    random.shuffle(qualifies_for_next_round)
    if len(not_compared_yet_this_round) == 1:
        qualifies_for_next_round.append(not_compared_yet_this_round.pop())

# --- End of function --- #





def compare(contender1: Pokemon, contender2: Pokemon) -> tuple[Pokemon, Pokemon]:
    winner: Pokemon
    loser: Pokemon

    answer: str = ""
    while not answer in ["0", "1"]:
        print(
            "Which of these Pokémon do you prefer?"
            f"\n{contender1.name} (0) or {contender2.name} (1) :"
        )
        answer = input()
    if answer == "0": winner, loser = contender1, contender2
    else: winner, loser = contender2, contender1

    winner.pokemons_it_has_defeated.append(loser)
    loser.pokemon_it_was_defeated_by = winner
    return winner, loser

# --- End of function --- #





if __name__ == "__main__": programLoop(main, t1, head_l)