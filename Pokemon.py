#  __________________________
# / \                        \
#|   |                        |
# \_/| ----------||---------- |
#    |                        |
#    |        Code by:        |
#    |   Élie-David langlois  |
#    |                        |
#    |         Pokemon        |
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

class Pokemon:
    type JSONPokemon = dict[str, int | str]

    next_unknown_no: int = -1

    def __init__(self, dex_no: int = 0, name: str = "Unknown") -> None:
        self.name: str = name
        if dex_no == 0:
            self.dex_no = Pokemon.next_unknown_no
            Pokemon.next_unknown_no -= 1
        else : self.dex_no: int = dex_no
    # --- End of function --- #





    def toJSON(self) -> Pokemon.JSONPokemon:
        poke_json: Pokemon.JSONPokemon = {}
        
        return poke_json
    # --- End of function --- #
# --- End of class Pokemon --- #