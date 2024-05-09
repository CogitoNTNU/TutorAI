# How to Start Docker for Django Backend
This guide will cover the steps needed to get The TutorAI environment set up using Docker.

## Prerequisites
Before you begin, ensure that you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

These tools are required to create your containerized environment.

## Steps to Start Docker
Navigate to the root of the project where the `docker-compose.yml` file is located.

Then run the following commands to build and start your Docker containers:

```bash
docker compose build # This command builds the Docker images defined in your docker-compose.yml file.
docker compose up    # This command starts the containers in the foreground. Add -d to run them in the background.
```

After running docker-compose up, your Django application should be accessible via `http://localhost:8000` or another port specified in your Docker configuration.

To stop your Docker containers, you can use:

```bash
docker compose down
```

To view the status of your Docker containers, you can use:
```bash
docker ps
```

## Running Django Commands
To run Django commands, you can use the following command:

```bash
docker compose run tutorai python manage.py <command>
```

Replace `<command>` with the Django command you want to run.
So to run tests, you can use:

```bash
docker compose run tutorai python manage.py test
```

### Running Django Migrations
To run Django migrations, you can use the following command:

```bash
docker compose run tutorai python manage.py makemigrations
docker compose run tutorai python manage.py migrate
```
