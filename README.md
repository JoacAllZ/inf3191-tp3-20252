# inf3191-tp3-20252

**Auteur :** Joachim Alladio-Zerbé

**Code Permanent :** ALLJ28099800

# Installation

Afin de pouvoir installer correctement l'application il faut s'assurer d'avoir les dépendances suivantes :

- `make`
- `python` version 3
- `python3[#version]-venv` pour environnement linux

Une fois le répertoire cloner aller dans la racine et installer l'environnement virtuel python :

```sh
make install
```

Il est possible de nettoyer l'environnemnt python si l'installation est corrompue avec :

```sh
make clean
```

Puis refaire l'installation.

# Exécution

Après avoir fais un `make install`, pour exécuter l'application :

```sh
make run
```

Flask indiquera le port d'exécution de l'application avec un url.

Exemple de sortie flask :

````sh
 * Serving Flask app 'index'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://<adresse local>:5000
```