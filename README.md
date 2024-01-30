# Updraft DRF Assignment

Welcome to the Updraft technical test! In this project, you will find a small Django web service configured with Django REST framework. The goal of this exercise is to build list and retrieve endpoints for the Account and Transaction models. Additionally, these endpoints have specific requirements that you should fulfill.

## Getting Started

Before you start working on the tasks, ensure you have set up your development environment:

1. Create a Python 3 virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install dependencies with Poetry:

    ```bash
    pip install poetry
    poetry install
    ```

3. Run the database migrations and load sample data:

    ```bash
    python manage.py migrate
    python manage.py loaddata sample.json
    ```

## Running Tests

We use `pytest` to run our tests. To execute the tests, run:

```bash
pytest
