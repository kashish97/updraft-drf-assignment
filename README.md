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


Task Overview
Your main tasks are to create both list and retrieve endpoints for the Account and Transaction models. The following URLs are expected to be supported:

GET /accounts/: List all bank accounts.
GET /accounts/:id: Retrieve the bank account with ID :id.
GET /transactions/: List all transactions.
GET /transactions/:id: Retrieve the transactions with ID :id.

Code Structure
accounts/: Django app for account-related models and views.
transactions/: Django app for transaction-related models and views.
API Endpoints
Accounts
GET /accounts/: List all bank accounts. Paginated using cursor-based pagination.
GET /accounts/:id: Retrieve the bank account with ID :id.
Additional fields in the Account object for API responses:

{
    "id": 1,
    "user": 2,
    "name": "John Smith",
    "transaction_count_last_thirty_days": 119,
    "balance_change_last_thirty_days": "-1304.67"
}

Authorization
Users can only see their own Accounts and Transactions. Admin users (User.is_staff) can view all accounts and transactions in the system.
