# Overview

A small project that uses FastAPI and Django and asyncio to work with a database using the Django ORM.
```
# Start Django
uvicorn testproject.asgi:application --reload

# Start FastAPI
uvicorn main:app --reload --port <port>
```