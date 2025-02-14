# Weather_App

Weather_App est une application météo légère développée principalement en Python qui utilise l'API OpenWeather.


L'application offre plusieurs fonctionnalités :
- Connaître la météo d'une ville. 
- Obtenir son taux de rayon UV ainsi que la qualité de l'air. 

## Comment faire fonctionner l'application ? 
Nous supposons que vous utilisez un environnement Debian/Ubuntu 

1. Clonez le dépôt Git et rendez-vous dans le répertoire ainsi créé :

    ```sh
    git clone https://github.com/Hiruzu/weather_app.git
    cd mining-weather
    ```

2. Vérifier que docker et docker-compose sont installés  :

    ```sh
    apt install -y docker docker-compose
    ```

## Comment exécuter l'application avec Docker ?

1. Créez un fichier `.env` contenant votre clé d'API OpenWeather ainsi que le port de fonctionnement de l'application :

    ```env
    OPENWEATHER_API_KEY=Votre_Clé_API
    PORT=3000
    ```

2. Démarrez l'application avec :

    ```sh
    docker compose up -d --build
    ```

3. Ouvrez un navigateur et accédez à l'adresse `http://localhost`.
