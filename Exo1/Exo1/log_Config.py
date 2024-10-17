import logging
#Configuration du logging
logging.basicConfig(filename= "../config.log", level= logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Fonction pour obtenir un logger
def get_logger(name):
    return logging.getLogger(name)