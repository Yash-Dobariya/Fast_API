from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'])

def hash_password(password : str):
    return password_context.hash(password)

def verify_password(hashed_password:str, password:str):
    return password_context.verify( hashed_password, password)