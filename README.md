# POS Sales Tracker REST API

This is a simple REST API for managing products, sales, and stores.

## Assumptions

The following assumptions were made during the design and implementation:

* The provided MySQL database schema is used.
* The API follows basic RESTful principles.
* Data is exchanged in JSON format.
* JWT is used for stateless authentication.
* Hourly sales summaries are generated at the top of each hour for the previous hour.
* The implementation prioritizes meeting core requirements with simplicity.
* User roles (cashier, sales manager, head office manager) are included in the JWT, but detailed role-based authorization on endpoints is not fully implemented beyond requiring authentication.
* Input data validation is primarily done using Marshmallow schemas.

## Instructions to Run

1.  **Clone the repository** (if applicable).
2.  **Ensure Python 3 is installed.**
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure the database:**
    * Open the `config.py` file.
    * Modify the `DATABASE_URI` to match your MySQL database connection details (username, password, host, port, database name).
5.  **Initialize the database** (if you haven't already using the MySQL script):
    Although you've already created the database using the MySQL script, Flask-SQLAlchemy will interact with it based on the models. You might not need to explicitly initialize it via Python if the schema is already set up.
6.  **Run the application:**
    ```bash
    python app.py
    ```
    The API will typically start at `http://127.0.0.1:5000/`.

## API Endpoints

* `POST /register`: Register a new user.
* `POST /login`: Get an authentication token.
* `GET /products`: Get all products.
* `GET /products/<product_id>`: Get a specific product.
* `GET /stores`: Get all stores.
* `GET /stores/<store_id>`: Get a specific store.
* `POST /sales`: Record a sale (requires authentication, send a list of items).
* `GET /inventory/<product_id>`: Get the inventory status of a product (requires authentication).
* `GET /stores/<store_id>/summaries`: Get hourly sales summaries for a store (requires authentication).

## Authentication

Most of the write and some read endpoints are protected by JWT authentication. You need to log in via `/login` to get a token and then include it in the `Authorization` header as a Bearer token.
