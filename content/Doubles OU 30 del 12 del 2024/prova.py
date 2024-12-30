import numpy as np

def calculate_effects(type_counts):
    # Matrice dei moltiplicatori di tipo (valori di esempio; da adattare con valori reali)
    type_chart = {
        'normal': {'rock': 0.5, 'ghost': 0, 'steel': 0.5},
        'fire': {'grass': 2, 'water': 0.5, 'rock': 0.5, 'bug': 2, 'steel': 2, 'ice': 2, 'dragon': 0.5},
        'water': {'fire': 2, 'water': 0.5, 'grass': 0.5, 'ground': 2, 'rock': 2, 'dragon': 0.5},
        'electric': {'water': 2, 'electric': 0.5, 'grass': 0.5, 'ground': 0, 'flying': 2, 'dragon': 0.5},
        'grass': {'water': 2, 'fire': 0.5, 'grass': 0.5, 'flying': 0.5, 'poison': 0.5, 'ground': 2, 'rock': 2, 'bug': 0.5, 'dragon': 0.5, 'steel': 0.5},
        'ice': {'fire': 0.5, 'water': 0.5, 'grass': 2, 'ice': 0.5, 'ground': 2, 'flying': 2, 'dragon': 2, 'steel': 0.5},
        'fighting': {'normal': 2, 'rock': 2, 'steel': 2, 'ice': 2, 'dark': 2, 'ghost': 0, 'poison': 0.5, 'flying': 0.5, 'psychic': 0.5, 'bug': 0.5, 'fairy': 0.5},
        'poison': {'grass': 2, 'poison': 0.5, 'ground': 0.5, 'rock': 0.5, 'ghost': 0.5, 'steel': 0, 'fairy': 2},
        'ground': {'fire': 2, 'electric': 2, 'grass': 0.5, 'poison': 2, 'flying': 0, 'bug': 0.5, 'rock': 2, 'steel': 2},
        'flying': {'electric': 0.5, 'grass': 2, 'fighting': 2, 'bug': 2, 'rock': 0.5, 'steel': 0.5},
        'psychic': {'fighting': 2, 'poison': 2, 'steel': 0.5, 'psychic': 0.5, 'dark': 0},
        'bug': {'grass': 2, 'fire': 0.5, 'fighting': 0.5, 'flying': 0.5, 'poison': 0.5, 'ghost': 0.5, 'steel': 0.5, 'fairy': 0.5, 'psychic': 2, 'dark': 2},
        'rock': {'fire': 2, 'ice': 2, 'fighting': 0.5, 'ground': 0.5, 'steel': 0.5, 'flying': 2, 'bug': 2},
        'ghost': {'normal': 0, 'psychic': 2, 'ghost': 2, 'dark': 0.5},
        'dragon': {'dragon': 2, 'steel': 0.5, 'fairy': 0},
        'dark': {'fighting': 0.5, 'psychic': 2, 'bug': 0.5, 'ghost': 2, 'dark': 0.5, 'fairy': 0.5},
        'steel': {'rock': 2, 'ice': 2, 'fairy': 2, 'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'steel': 0.5},
        'fairy': {'fighting': 2, 'dragon': 2, 'dark': 2, 'fire': 0.5, 'poison': 0.5, 'steel': 0.5},
    }

    # Lista di tutti i tipi
    all_types = type_chart.keys()

    # Inizializza le debolezze, resistenze e immunità
    effectiveness = {t: 1.0 for t in all_types}

    # Calcola l'efficacia basata sui conteggi dei tipi
    for p_type, count in type_counts.items():
        if p_type in type_chart:
            for target_type, multiplier in type_chart[p_type].items():
                effectiveness[target_type] *= multiplier ** count

    # Classifica le debolezze, resistenze e immunità
    weaknesses = [t for t, e in effectiveness.items() if e > 1]
    resistances = [t for t, e in effectiveness.items() if 0 < e < 1]
    immunities = [t for t, e in effectiveness.items() if e == 0]

    return weaknesses, resistances, immunities

# Esempio di input
type_counts = {'fire': 31, 'dark': 34, 'grass': 30, 'water': 32, 'ground': 24, 'flying': 27, 'ghost': 22, 'fighting': 30, 'electric': 13, 'ice': 12, 'fairy': 26, 'steel': 28, 'dragon': 21, 'rock': 17, 'poison': 16, 'normal': 22, 'psychic': 40, 'bug': 6}

# Calcola le debolezze, resistenze e immunità
weaknesses, resistances, immunities = calculate_effects(type_counts)

print("Debolezze:", weaknesses)
print("Resistenze:", resistances)
print("Immunità:", immunities)
