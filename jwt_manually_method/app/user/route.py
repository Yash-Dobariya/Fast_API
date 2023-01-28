from fastapi import Depends, HTTPException, status, APIRouter
from app.user.schemas import SignupUser, DisplayUser, LoginUser
from app.user.model import User
from sqlalchemy.orm import Session
from app.utils.password import hash_password, verify_password
from app.database import get_db
from app.utils.token import create_access_token, create_refresh_token


user_routes = APIRouter()

# Register page
@user_routes.post('/signup', response_model = DisplayUser)
async def get_details_signup(request : SignupUser, db : Session = Depends(get_db)):
    new_user = User(name = request.name, 
                    password = hash_password(request.password),
                    first_name = request.first_name, 
                    last_name = request.last_name,
                    email = request.email, 
                    gender = request.gender,
                    role = request.role)
    db.add(new_user)
    db.commit()
    return new_user

# Login page
@user_routes.post('/signin')
async def get_details_signin(user : LoginUser, db : Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    user_email = db_user.email
    db_user_password = db_user.password
    db_id = str(db_user.id)
    user_token = {'user_id' : db_id, 'user_name' : db_user.name, 'user_email' : db_user.email}
    
    if user_email and verify_password( user.password, db_user_password):
 
        access_token = create_access_token(user_token)
        refresh_token = create_refresh_token(user_token)

        return {"access_token":access_token, "refresh_token":refresh_token}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="wrong email id and password 😢")