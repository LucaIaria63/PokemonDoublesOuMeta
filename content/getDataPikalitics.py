import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from rich.console import Console
import datetime
import ast
import os

# Ottieni la data e l'ora correnti
oggi = datetime.date.today()

print(oggi)

percorso_corrente = os.path.dirname(os.path.abspath(__file__))
percorso_completo = os.path.join(percorso_corrente, f"{oggi}")
os.makedirs(percorso_completo, exist_ok=True)


console = Console()

type_chart = {
    "normal": {"rock": 0.5, "ghost": 0, "steel": 0.5},
    "fire": {"grass": 2, "ice": 2, "bug": 2, "steel": 2, "fire": 0.5, "water": 0.5, "rock": 0.5, "dragon": 0.5},
    "water": {"fire": 2, "ground": 2, "rock": 2, "water": 0.5, "grass": 0.5, "dragon": 0.5},
    "electric": {"water": 2, "flying": 2, "electric": 0.5, "grass": 0.5, "ground": 0},
    "grass": {"water": 2, "ground": 2, "rock": 2, "fire": 0.5, "grass": 0.5, "poison": 0.5, "flying": 0.5, "bug": 0.5, "dragon": 0.5, "steel": 0.5},
    "ice": {"grass": 2, "ground": 2, "flying": 2, "dragon": 2, "fire": 0.5, "water": 0.5, "ice": 0.5, "steel": 0.5},
    "fighting": {"normal": 2, "ice": 2, "rock": 2, "dark": 2, "steel": 2, "poison": 0.5, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "ghost": 0, "fairy": 0.5},
    "poison": {"grass": 2, "fairy": 2, "poison": 0.5, "ground": 0.5, "rock": 0.5, "ghost": 0.5, "steel": 0},
    "ground": {"fire": 2, "electric": 2, "poison": 2, "rock": 2, "steel": 2, "grass": 0.5, "bug": 0.5, "flying": 0},
    "flying": {"grass": 2, "fighting": 2, "bug": 2, "electric": 0.5, "rock": 0.5, "steel": 0.5},
    "psychic": {"fighting": 2, "poison": 2, "psychic": 0.5, "dark": 0, "steel": 0.5},
    "bug": {"grass": 2, "psychic": 2, "dark": 2, "fire": 0.5, "fighting": 0.5, "poison": 0.5, "flying": 0.5, "ghost": 0.5, "steel": 0.5, "fairy": 0.5},
    "rock": {"fire": 2, "ice": 2, "flying": 2, "bug": 2, "fighting": 0.5, "ground": 0.5, "steel": 0.5},
    "ghost": {"psychic": 2, "ghost": 2, "normal": 0, "dark": 0.5},
    "dragon": {"dragon": 2, "steel": 0.5, "fairy": 0},
    "dark": {"psychic": 2, "ghost": 2, "fighting": 0.5, "dark": 0.5, "fairy": 0.5},
    "steel": {"ice": 2, "rock": 2, "fairy": 2, "fire": 0.5, "water": 0.5, "electric": 0.5, "steel": 0.5},
    "fairy": {"fighting": 2, "dragon": 2, "dark": 2, "fire": 0.5, "poison": 0.5, "steel": 0.5}
}

def calculate_weakness(defender_types, attacking_type):
    multiplier = 1.0
    for defender_type in defender_types:
        try:
            multiplier *= type_chart[attacking_type][defender_type]
        except:
            multiplier *=1
    return multiplier

def display_progress(iteration, total):
    bar_max_width = 30
    bar_current_width = bar_max_width * iteration // total
    bar = "█" * bar_current_width + "-" * (bar_max_width - bar_current_width)
    progress = "%.1f" % (iteration / total * 100)
    console.print(f"|{bar}| {progress} % {iteration}/{total}", end="\r", style="bold green")
    if iteration == total:
        print()

def fetch_teammates(pokemon_name):
    if pokemon_name[-3]+pokemon_name[-2]+pokemon_name[-1]=="%20":pokemon_name=pokemon_name[:-3]
    while pokemon_name[-1]==" ":pokemon_name=pokemon_name[:-1]

    formatted_name = pokemon_name.replace(' ', '').capitalize()
    url = f"https://www.pikalytics.com/pokedex/gen9doublesou/{formatted_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        teammates_section = soup.find('div', {'id': 'dex_team_wrapper'})
        typePokemon = soup.find('span', {'class': 'inline-block pokedex-header-types'})
        usage_singolo = soup.find('div', {'class': 'pokemon-ind-summary-text gold-font'})
        items_section = soup.find('div', {'class': 'dex-items-wrapper'})
        
        types = []
        for Type in typePokemon.find_all('span'):
            types.append(Type.text)
        if len(types)==0: types = ["NonTrovato"]

        if not teammates_section:
            print(f"Non sono stati trovati compagni di squadra per {pokemon_name}.")
            return [[{'name': "NotFound", 'usage': "0%" }], types, usage_singolo.text, []]
        
        teammates = []
        for entry in teammates_section.find_all('a', class_='teammate_entry'):
            name = entry['data-name'].strip() if 'data-name' in entry.attrs else "Sconosciuto"
            
            percentage_div = entry.find('div', style="display:inline-block;float:right;")
            percentage = percentage_div.text.strip() if percentage_div else "0%"
            
            teammates.append({'name': name, 'usage': percentage})

        items = []
        if items_section:
            for entry in items_section.find_all('a', class_='item_entry'):
                item_name = entry['data-name'].strip() if 'data-name' in entry.attrs else "Sconosciuto"
                
                item_percentage_div = entry.find('div', style="display:inline-block;float:right;")
                item_percentage = item_percentage_div.text.strip() if item_percentage_div else "0%"
                
                items.append({'item': item_name, 'usage': item_percentage})

        return [teammates, types, usage_singolo.text, items]
    
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta per {pokemon_name}: {e}")
        types = ["NonTrovato"]
        return [[{'name': "NotFound", 'usage': "0%" }], types, "0%", []]


pokemon = "Incineroar" 
data = fetch_teammates(pokemon)
teammates_pokemon_list = {pokemon : data}
pokemon_list = [pokemon]
try:
    while True:
        lista_copia = list(teammates_pokemon_list.keys())
        for pokemonn in lista_copia:
            for pokemon2 in teammates_pokemon_list[pokemonn][0]:
                if pokemon2["name"] not in pokemon_list and pokemon2!="NotFound":
                    teammates = fetch_teammates(pokemon2["name"])
                    pokemon_list.append(pokemon2["name"])
                    teammates_pokemon_list[pokemon2["name"]] = teammates
            display_progress(len(pokemon_list),262)
        if len(pokemon_list)>= 262: break
except KeyboardInterrupt:
    pass

tipi_finali = {}
for Nome_File in list(teammates_pokemon_list.keys()):
    string = ""
    copia_nome_file = Nome_File
    if Nome_File[-3]+Nome_File[-2]+Nome_File[-1]=="%20": Nome_File=Nome_File[:-3]
    while Nome_File[-1]==" ": Nome_File=Nome_File[:-1]
    with open(os.path.join(percorso_completo, f"{unquote(Nome_File)}.md"), "w") as f:
        string = """---
tags:"""
        for tipi in teammates_pokemon_list[copia_nome_file][1]:
            string += f"\n- {tipi}"
        try:
            tipi_finali[f"{teammates_pokemon_list[copia_nome_file][1]}"] += 1
        except:
            tipi_finali[f"{teammates_pokemon_list[copia_nome_file][1]}"] = 1
        string += "\n---"
        string += f"\n# Usage\n- {teammates_pokemon_list[copia_nome_file][2]}"
        string += "\n# Teammates"
        for nome in teammates_pokemon_list[copia_nome_file][0]:
            vero_nome = nome["name"]
            while vero_nome[-1] == " ": vero_nome = vero_nome[:-1]
            if vero_nome[-3] + vero_nome[-2] + vero_nome[-1] == "%20": vero_nome = vero_nome[:-3]
            while vero_nome[-1] == " ": vero_nome = vero_nome[:-1]
            usage = nome["usage"]
            string += f"\n- [[{unquote(vero_nome)}]] : {usage}"

        string += "\n# Items"
        for item in teammates_pokemon_list[copia_nome_file][3]:
            item_name = item["item"]
            item_usage = item["usage"]
            string += f"\n- {item_name} : {item_usage}"

        f.write(string)

Archetipi = {}
x = 1
for pokemons in list(teammates_pokemon_list.keys()):
    lista = [pokemons]
    for teammates in teammates_pokemon_list[pokemons][0]:
        if float(teammates["usage"].strip('%')) >25 and float(teammates_pokemon_list[pokemons][2].strip('%'))>5:
            lista.append(teammates["name"])
    Archetipi[x] = lista
    x+=1

weaknessses = {}
for tipo in type_chart.keys():weaknessses[tipo] = 1
for elemento in tipi_finali:
    itipi = ast.literal_eval(elemento)
    for typing in type_chart.keys():
        debolezza = calculate_weakness(itipi, typing)
        if debolezza==2.0:
            weaknessses[typing]+=1
        elif debolezza==0.0:
            weaknessses[typing]-=1
        elif debolezza==0.5:
            weaknessses[typing]-=1

print("\n")
string = "# Resoconto"
cattivi = ""
medi = ""
buoni = ""
lista_dei_cattivi = {}
lista_dei_buoni = {}
lista_dei_medi = {}
weaknessses = dict(sorted(weaknessses.items(), key=lambda item: item[1]))
for typing in weaknessses.keys():
    if weaknessses[typing]<0:
        lista_dei_cattivi[typing] = weaknessses[typing]
        lista_dei_cattivi = dict(sorted(lista_dei_cattivi.items(), key=lambda item: item[1]))
    elif weaknessses[typing]>0:
        lista_dei_buoni[typing] = weaknessses[typing]
        lista_dei_buoni = dict(sorted(lista_dei_buoni.items(), key=lambda item: item[1]))
    else:
        lista_dei_medi[typing] = weaknessses[typing]
for item in lista_dei_buoni.keys():
    string+=f"\n- #{item} : =={lista_dei_buoni[item]}=="
for item in lista_dei_medi.keys():
    string+=f"\n- #{item} : {lista_dei_medi[item]}"
for item in lista_dei_cattivi.keys():
    string+=f"\n- #{item} : {lista_dei_cattivi[item]}"
with open(os.path.join(percorso_completo, f"Resoconto.md"),"w") as f:
    f.write(string)

copiaArchetipi = Archetipi
for Archetipo in list(copiaArchetipi.keys()):
    if len(copiaArchetipi[Archetipo])<=1:
        Archetipi.pop(Archetipo)
        
string = "# Archetipi:"
for Archetipo in Archetipi.keys():
    string+=f"\n## Archetipo n°{Archetipo}: "
    for pokemon in Archetipi[Archetipo]:
        string+=f"\n- {unquote(pokemon)}"
with open(os.path.join(percorso_completo, f"Archetipi.md"), "w") as f:
    f.write(f"{string}")

string=f"""---
title Dati finali
---
# Ultimo aggiornamento
- [[{oggi}\\Resoconto]]
- [[{oggi}\\Archetipi]]"""

with open(os.path.join(percorso_corrente, "index.md") as f:
    f.write(f"{string}")
