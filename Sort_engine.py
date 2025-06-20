def get_key_func(keys):
    """Génère une fonction d'extraction de clé de tri à partir d'une liste de colonnes"""
    def key_func(row):
        return tuple(row[key] for key in keys)
    return key_func

def insertion_sort(data, keys):
    """
    Tri par insertion stable en place
    - data : liste de dictionnaires (en place)
    - keys : liste des colonnes de tri (ordre de priorité)
    """
    key_func = get_key_func(keys)
    n = len(data)
    
    for i in range(1, n):
        current = data[i]
        current_key = key_func(current)
        j = i - 1
       
        while j >= 0 and key_func(data[j]) > current_key:
            data[j + 1] = data[j]
            j -= 1
            
        data[j + 1] = current

def merge_sort(data, keys):
    """
    Tri fusion récursif stable (retourne une nouvelle liste)
    - data : liste de dictionnaires
    - keys : liste des colonnes de tri
    Retourne nouvelle liste triée
    """
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = merge_sort(data[:mid], keys)
    right = merge_sort(data[mid:], keys)
    return _merge(left, right, get_key_func(keys))

def _merge(left, right, key_func):
    """Fusionne deux listes triées"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# APPELS DES FONCTIONS 

"Données de test"

data_people = [
    {"nom": "Donic", "age": 25, "ville": "Kisangani"},
    {"nom": "Isaac", "age": 30, "ville": "Goma"},
    {"nom": "Jules", "age": 20, "ville": "Lubumbashi"},
    {"nom": "Samuel", "age": 25, "ville": "Bunia"}
]

"Test de insertion_sort (tri en place)"

data_insertion = data_people.copy()
insertion_sort(data_insertion, ["nom", "age"])
print("Résultat du tri par insertion:")
for item in data_insertion:
    print(item)

"Test de merge_sort (retourne une nouvelle liste triée)"

sorted_data = merge_sort(data_people, ["ville", "nom"])
print("\nRésultat du tri fusion:")
for item in sorted_data:
    print(item)