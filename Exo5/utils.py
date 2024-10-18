import random

def couleur(nombre):
    """Renvoie la couleur (noir ou blanc) en fonction du nombre."""
    if nombre % 2 == 0:
        return "noir"  # Nombres pairs sont noirs
    else:
        return "blanc"  # Nombres impairs sont blancs

def calculer_gain(mise, nombre_roulette, nombre_joueur):
    """Calcule le gain en fonction du nombre choisi et de la roulette."""
    if nombre_roulette == nombre_joueur:
        return mise * 3  # Gagner 3x la mise si le nombre exact est trouvé
    elif couleur(nombre_roulette) == couleur(nombre_joueur):
        return int(mise * 1.5)  # Gagner 50% de la mise si même couleur
    else:
        return 0  # Rien gagné si ni le nombre ni la couleur ne correspond

def lancer_roulette():
    """Lance la roulette et retourne un nombre entre 0 et 49."""
    return random.randint(0, 49)