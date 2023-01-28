from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'])

def hash_password(password: str):
    return context.hash(password)

def verify_password(hash_password: str, password:str):
    return context.verify(hash_password, password)