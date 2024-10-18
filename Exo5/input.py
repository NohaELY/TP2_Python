def demander_nombre():
    """Demande à l'utilisateur un nombre entre 0 et 49."""
    while True:
        try:
            nombre = int(input("Choisissez un nombre entre 0 et 49 : "))
            if 0 <= nombre <= 49:
                return nombre
            else:
                print("Le nombre doit être entre 0 et 49.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

def demander_mise(solde):
    """Demande à l'utilisateur de miser un montant valide."""
    while True:
        try:
            mise = int(input(f"Votre solde est de {solde}€. Combien voulez-vous miser ? "))
            if 0 < mise <= solde:
                return mise
            else:
                print(f"Vous devez miser un montant entre 1 et {solde}€.")
        except ValueError:
            print("Veuillez entrer un montant valide.")