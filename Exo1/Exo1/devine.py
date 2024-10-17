#Exo 1 
import random
import logging
#Configuration du logging
logging.basicConfig(filename='config.log',level= logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def deviner_le_nombre():
    num_Devine = random.randint(1, 100)
    proposition = None
    print("Le jeu a commencé. Nombre à deviner :")
    logging.info("Le jeu a commencé. Nombre à deviner : %d", num_Devine)

    print("Bienvenue: ")

    while proposition != num_Devine:
        try:
            # Demander à l'utilisateur de saisir un nombre entier
            proposition = int(input("Saisir un nombre entier entre 1 et 100: "))
            logging.info("Utilisateur a proposé : %d", proposition)

            if proposition == num_Devine:
                print("Bravooo!!!")
                logging.info("Utilisateur a trouvé le nombre : %d", num_Devine)
            elif proposition < num_Devine:
                print("Trop petit!!!")
                logging.info("Nombre trop petit")
            else:
                print("Trop grand!!!")
                logging.info("Nombre trop grand")
        except ValueError as e:
            print("Saisir un entier: ")
            #logging.warning("Entrée non valide, utilisateur n'a pas saisi un entier. Erreur : %s", e)

def main():
    logging.info("Démarrage du programme")
    try:
        deviner_le_nombre()
    except Exception as e:
        logging.error("Une erreur s'est produite : %s", e)
    logging.info("Fin du programme")

# Appel à la fonction main si ce fichier est exécuté directement
if __name__ == "__main__":
    main()