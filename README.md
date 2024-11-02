# Flask User Management API : LAB 5 EECE 435L

## Overview
This Flask application provides a RESTful API for managing user information stored in an SQLite database. It supports operations to create, read, update, and delete (CRUD) user data.

## Features
- **List all users**: Retrieve a JSON list of all registered users.
- **Retrieve user by ID**: Fetch detailed information of a specific user by their unique identifier.
- **Add new user**: Create a new user entry in the database.
- **Update user information**: Modify existing user details by ID.
- **Delete user**: Remove a user from the database by ID.

## Technologies
- Flask
- SQLite
- Postman for testing API endpoints

## Getting Started

### Prerequisites
- Python 3
- Flask
- SQLite

### Setup and Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd your-repository
    ```
3. **Install required Python packages**:
    ```bash
    pip install Flask sqlite3
    ```
4. **Initialize the database**:
    ```bash
    python database.py
    ```
5. **Run the application**:
    ```bash
    python app.py
    ```

## API Routes
- `GET /api/users`: List all users
- `GET /api/users/<int:user_id>`: Get a user by ID
- `POST /api/users`: Add a new user
- `PUT /api/users/<int:user_id>`: Update a user's information
- `DELETE /api/users/<int:user_id>`: Delete a user

## Testing
Test the API using Postman or any other API client by navigating to:
`http://localhost:5000/api/users`
