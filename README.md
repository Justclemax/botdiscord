# Botdiscord

## À propos de ce projet

Ce projet implémente un bot Discord en utilisant la bibliothèque discord.py. Suivez les étapes ci-dessous pour commencer.

### Étapes d'installation

1. **Créer un compte Discord sur le site Discord :**
   - Allez sur [Discord](https://discord.com) et créez un compte si vous n'en avez pas déjà un.

2. **Cloner le projet et Installer l'environnement virtuel :**
   - Ouvrez votre terminal et exécutez les commandes suivantes :
     ```bash
     git clone https://github.com/Justclemax/botdiscord.git
     cd botdiscord
     ```
   - Ensuite, créez un environnement virtuel nommé "env" en exécutant la commande suivante :
     ```bash
     python -m venv env
     ```


3. **Activer l'environnement virtuel :**
   - Sur Windows, exécutez la commande :
     ```bash
     .\env\Scripts\activate
     ```
   - Sur macOS/Linux, exécutez la commande :
     ```bash
     source env/bin/activate
     ```

4. **Installer les dépendances :**
   - Avec l'environnement virtuel activé, installez les packages nécessaires à l'aide de la commande suivante :
     ```bash
     pip install -r requirements.txt
     ```
     Assurez-vous d'avoir un fichier `requirements.txt` contenant les dépendances nécessaires.

### Création

Pour une démonstration visuelle de la création d'un bot Discord, vous pouvez suivre cette vidéo :

<video width="400" height="400" controls
    src="https://github.com/Justclemax/botdiscord/assets/90102062/9ff778df-fd03-4a72-aa03-410021fb1958"> 
    Votre navigateur ne prend pas en charge la balise vidéo.
</video>



Assurez-vous de consulter la vidéo pour des instructions détaillées sur le processus de création du bot Discord.

### Configuration du Bot

1. **Token Discord :**
   - Obtenez votre token Discord depuis [le portail des développeurs Discord](https://discord.com/developers/applications).
   - Créez un fichier `.env` à la racine du projet et ajoutez votre token :
     ```env
     DISCORD_TOKEN=VotreTokenDiscord
     ```
   - Assurez-vous de ne pas partager votre fichier .env publiquement pour éviter la divulgation de vos informations sensibles. Pour plus de détails sur l'utilisation de python-dotenv, consultez la [documentation officielle](https://pypi.org/project/python-dotenv/).

2. **Configurer d'autres paramètres :**
   - Consultez la documentation de discord.py et ajustez les paramètres du bot selon vos besoins. Pour plus d'informations, consultez la [documentation de discord.py](https://discordpy.readthedocs.io/en/stable/).

### Exécuter le Bot

- Exécutez le bot en utilisant la commande :
  ```bash
  python bot.py run
