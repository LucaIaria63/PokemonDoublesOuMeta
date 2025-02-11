import json
import networkx as nx
import turtle
from alphabeter import *

def main():
    # Carica il file JSON
    with open('team_dict.json', 'r') as f:
        team_data = json.load(f)


    # Aggiungi archi basati sui team
    for team in team_data.values():
        for i, pokemon1 in enumerate(team):
            printData(pokemon1)
            for pokemon2 in team[i+1:]:
                printData(pokemon2)



if __name__ == '__main__':
    main()
    turtle.done()