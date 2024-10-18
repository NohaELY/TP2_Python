from setuptools import setup, find_packages

setup(
    name='Exo5',
    version='0.1.0',
    description="Un jeu où l'utilisateur doit deviner un nombre entre 1 et 100",
    author='Nohaila',
    packages=find_packages(),
    install_requires=[],  # pour installer les packages
    entry_points={
        'console_scripts': [
            'devine_nombre=devine_nombre.Exo1:deviner_le_nombre',  # Point d'entrée pour exécuter le jeu depuis la ligne de commande juste en tapant devine_npmbre
        ],
    },
)
