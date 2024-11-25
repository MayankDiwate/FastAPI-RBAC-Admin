# FastAPI RBAC

This is a FastAPI-based application that provides user authentication and management features. It includes endpoints for user registration, signing in, and signing out, utilizing secure token-based authentication.

## Features
- **User Registration**: Register new users with unique usernames.
- **User Login**: Authenticate users and issue JWT tokens.
- **User Logout**: Simulated sign-out for token-based systems.

## Requirements
- Python 3.10 or higher
- FastAPI
- SQLAlchemy
- Uvicorn
- Any additional dependencies (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:MayankDiwate/FastAPI-RBAC-Admin.git
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. Access the application at:
   ```
   http://localhost:8000/docs
   ```

## Docker Support

To build and run the application in a Docker container:

1. Build the Docker image:
   ```bash
   docker build -t fastapi-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 fastapi-app
   ```

3. Access the application at:
   ```
   http://localhost:8000/docs
   ```

## Usage
- Use the `/register` endpoint to create a new user.
- Authenticate with the `/sign-in` endpoint to obtain a JWT token.
- Test APIs with the interactive Swagger UI at `/docs`.

## License
This project is licensed under the MIT License.
