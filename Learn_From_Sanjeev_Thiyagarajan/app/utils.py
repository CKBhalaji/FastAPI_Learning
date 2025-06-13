from passlib.context import CryptContext
import bcrypt  

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_p(password: str):
    return pwd_context.hash(password)

def verify_p(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)