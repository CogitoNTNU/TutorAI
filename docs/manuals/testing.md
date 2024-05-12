# Testing
The project uses both frontend and backend testing. The backend uses Django's built-in testing framework, while the frontend uses Vitest.

## Backend

To run all the tests, run the following command in the `backend` directory of the project:

```bash
docker-compose run tutorai python manage.py test flashcards
```

## Frontend
To run all the tests, run the following command in the `frontend` directory of the project:

```bash
npm run test
```
