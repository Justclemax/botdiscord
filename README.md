# Botdiscord
## À propos de ce projet

Ce projet implémente un bot Discord en utilisant le site Decord. Suivez les étapes ci-dessous pour commencer.

### Étapes d'installation

1. **Créer un compte Discord sur le site Decord:**
   - Allez sur [Decord](https://descord.com) et créez un compte si vous n'en avez pas déjà un.

2. **Cloner le projet et Installer l'environnement virtuel:**
     - Ouvrez votre terminal et exécutez la commande suivante :
     ``` bash
     git clone https://github.com/Justclemax/botdiscord.git
     ```
      ``` bash
        cd botdiscord 
     ```
    
   - Ouvrez votre terminal et exécutez la commande suivante pour créer un environnement virtuel nommé "env":

     ```bash
     python -m venv env
     ```

3. **Activer l'environnement virtuel:**
   - Sur Windows, exécutez la commande :
     ```bash
     .\env\Scripts\activate
     ```
   - Sur macOS/Linux, exécutez la commande :
     ```bash
     source env/bin/activate
     ```

4. **Installer les dépendances:**
   - Avec l'environnement virtuel activé, installez les packages nécessaires à l'aide de la commande suivante :
     ```bash
     pip install -r requirements.txt
     ```
     Assurez-vous d'avoir un fichier `requirements.txt` contenant les dépendances nécessaires.

### Configuration du Bot

1. **Token Discord:**
   - Obtenez votre token Discord depuis [le portail des développeurs Discord](https://discord.com/developers/applications).
   - Créez un fichier `.env` à la racine du projet et ajoutez votre token :
     ```env
     DISCORD_TOKEN=VotreTokenDiscord
     ```

2. **Configurer d'autres paramètres:**
   - Consultez la documentation de Decord et ajustez les paramètres du bot selon vos besoins.

### Exécuter le Bot

- Exécutez le bot en utilisant la commande :
  ```bash
  python bot.py
