from input import demander_nombre, demander_mise
from utils import calculer_gain, lancer_roulette

def jouer_partie(solde):
    """Joue une partie du ZCasino et renvoie le nouveau solde."""
    nombre_joueur = demander_nombre()  # L'utilisateur choisit un nombre
    mise = demander_mise(solde)  # L'utilisateur mise une somme d'argent

    # Lancer la roulette
    nombre_roulette = lancer_roulette()
    print(f"La roulette a choisi le nombre {nombre_roulette} ({'noir' if nombre_roulette % 2 == 0 else 'blanc'})")

    # Calculer le gain
    gain = calculer_gain(mise, nombre_roulette, nombre_joueur)
    
    if gain > 0:
        print(f"Félicitations ! Vous avez gagné {gain}€.")
    else:
        print("Dommage, vous n'avez rien gagné cette fois.")

    # Mise à jour du solde
    solde += gain - mise
    return solde