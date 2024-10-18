from game import jouer_partie

def main():
    print("Bienvenue au ZCasino !")

    # Initialisation du solde
    solde = 100  # Par exemple, le joueur commence avec 100€

    while solde > 0:
        print(f"Votre solde actuel est de {solde}€.")
        solde = jouer_partie(solde)

        # Demander si le joueur veut continuer à jouer
        continuer = input("Voulez-vous rejouer ? (oui/non) : ").lower()
        if continuer != "oui":
            print(f"Vous quittez le jeu avec {solde}€. Merci d'avoir joué !")
            break

    if solde <= 0:
        print("Vous n'avez plus d'argent pour jouer. Merci d'avoir joué !")

if __name__ == "__main__":
    main()