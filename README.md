### Project Description ###

This project introduces a non-monolithic architecture which utilises some of the docker-compose potential.

The overall composition can be seen here:

![fastapi-clients (1)](https://github.com/user-attachments/assets/43884ace-268f-43da-acd0-b4415bb212f3)

List of main tools and images used:
- fastapi
- uvicorn
- pydantic
- mongodb
- mongo-express (as a dbclient)
- nginx
- docker-compose

The core module is a RESTful application which supports basic CRUD operations to manipulate data with the state stored in a MongoDB.

Here is a **Swagger** list of all supported operations:

![image](https://github.com/user-attachments/assets/07bf3fa9-6a74-425b-ad3a-e54aa17704ec)

Below you'll see general instructions on deploying or running the app manually.
## Deploying

The project is meant to be deployed by using **docker-compose**. 

Just run the command from the project's root directory providing a password env variable:
```
MONGO_PASSWORD=<password> docker compose up -d
```
That's all you need to deploy everything mentioned above.

You've got two ports available (ip for localhost):
```
127.0.0.1:80    # nginx -> uvicorn -> fastapi requests forwarding
127.0.0.1:8081  # ui client for mongodb using mongo-express image
```
Now you are ready to use something like **Curl** / **Postman** to test the application's endpoints, although you may want to look through **Swagger** docs on the `/docs` endpoint beforehand.

*Do notice that mongo-express is integrated for easy mongodb accessing and should be discarded in real world scenarios (or at least make sure you don't expose it's port for public access).*
## Manual app running
To run the app manually or make your own docker image you should remember to provide `DB_NAME` and `MONGODB_URL` environment variables.

The app supports reading the env variables from `.env` file, so you can place it in the project's root directory and populate it accordingly:
```
MONGODB_URL=mongodb://login:password@localhost:port/
DB_NAME=clientsDB
```
Now you can proceed with setting up `venv` and/or installing dependencies from `requirements.txt`.
