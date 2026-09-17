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
#    |        Project:        |
#    |      PokemonPicker     |
#    |                        |
#    |        Created:        |
#    |      Fr 2025-11-14     |
#    |      Version: 0.1      |
#    |                        |
#    |      Last update:      |
#    |      Th 2026-09-17     |
#    |      Version: 0.3      |
#    |                        |
#    | ----------||---------- |
#    |   _____________________|___
#    |  /                        /
#    \_/________________________/



from time import time
from Projects.Python_Utils.Templates.ProgramLoop2 import programLoop
t1: float = time()
head_l: int = 50

from Projects.PokemonPicker.Pokemon import Pokemon
from Projects.PokemonPicker.Ranking import RankingSession





names: list[str] = ["Bulbasaur", "Ivysaur", "Venusaur",
                    "Charmander", "Charmeleon", "Charizard",
                    "Squirtle", "Wartortle", "Blastoise"]
    
pokemons: list[Pokemon] = [Pokemon(i + 1, names[i]) for i in range(len(names))]



def main() -> None:
    session: RankingSession[Pokemon] = RankingSession(pokemons)
    session.run()
# --- End of function --- #





if __name__ == "__main__": programLoop(main, t1, head_l)