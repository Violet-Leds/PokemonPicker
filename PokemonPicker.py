#  __________________________
# / \                        \
#|   |                        |
# \_/| ----------||---------- |
#    |                        |
#    |        Code by:        |
#    |       Violet-Leds      |
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
#    |      We 2026-09-18     |
#    |     Version: 0.2.1     |
#    |                        |
#    | ----------||---------- |
#    |   _____________________|___
#    |  /                        /
#    \_/________________________/

from Projects.PokemonPicker.Pokemon import Pokemon
from Projects.PokemonPicker.Ranking import RankingSession



def main() -> None:
    names: list[str] = ["Bulbasaur", "Ivysaur", "Venusaur",
                        "Charmander", "Charmeleon", "Charizard",
                        "Squirtle", "Wartortle", "Blastoise"]
    
    pokemons: list[Pokemon] = [Pokemon(i + 1, names[i])
                               for i in range(len(names))]
    
    session: RankingSession[Pokemon] = RankingSession(pokemons)
    session.run()
# --- End of function --- #





if __name__ == "__main__": main()