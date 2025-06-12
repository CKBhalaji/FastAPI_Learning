# In this, we use the Python FastAPI and Postgresql

## 1. Navigate to your project directory:

```sh
cd path/to/your/project
```

## 2. Create the virtual environment:

```sh
python -m venv venv
```

## 3. Activate the virtual environment:

On Windows (Command Prompt):

```sh
venv\Scripts\activate.bat
```

On Windows (PowerShell):

```sh
.\venv\Scripts\Activate.ps1
```

How to confirm it's activated:

```sh
(venv) PS path/of/your/project
```

## 3. Install Dependencies:
```sh
pip install "fastapi[all]" uvicorn sqlalchemy pydantic "passlib[bcrypt]" python-jose[cryptography] psycopg2-binary python-dotenv
```
 --fastapi[all]: Core FastAPI, includes Uvicorn and Pydantic.<br>
 --sqlalchemy: ORM for database interaction.<br>
 --pydantic: Data validation and serialization (already part of fastapi[all], but good to be aware of).<br>
 --passlib[bcrypt]: For secure password hashing with bcrypt.<br>
 --python-jose[cryptography]: For JWT (JSON Web Token) creation and verification. Cryptography is needed for stronger algorithms.<br>
 --psycopg2-binary: PostgreSQL adapter.<br>
 --python-dotenv: To load environment variables from a .env file.<br>

  
## 4.To Start Your Project

 --Ensure PostgreSQL is running and you have created the database specified in your DATABASE_URL.<br>
 --Activate your virtual environment.<br>

 --> Start your FastAPI application:<br>

```sh
uvicorn main:app --reload
```
or
```sh
fastapi dev main.py (if inside the folder, add the folder name before the main.py)
```

 --Now, your FastAPI application will be running, accessible typically at http://127.0.0.1:8000. <br>
 --You can access the auto-generated documentation at http://127.0.0.1:8000/docs (Swagger UI) or http://127.0.0.1:8000/redoc (ReDoc) to interact with your API.<br>

⬆ Return to Top
