from fastapi import Depends, HTTPException, status, APIRouter
from app.user.schemas import SignupUser, DisplayUser, LoginUser
from app.user.model import User
from sqlalchemy.orm import Session
from app.utils.password import hash_password, verify_password
from app.database import get_db
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from app.utils.token import get_config


user_routes = APIRouter()

# Register page
@user_routes.post('/signup', response_model = DisplayUser)
async def get_details_signup(new_user : SignupUser, db : Session = Depends(get_db)):
    # try:
    create_user = User(name = new_user.name,
                        password = hash_password(new_user.password),
                        first_name = new_user.first_name,
                        last_name = new_user.last_name,
                        email = new_user.email,
                        gender = new_user.gender,
                        role = new_user.role)

    db.add(create_user)
    db.commit()
    return create_user
    # except:
    #     raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Please Sign-up ")

# Login page
@user_routes.post('/signin')
async def get_details_signin(user : LoginUser, Authorize : AuthJWT = Depends(get_config), db : Session = Depends(get_db)):
    try:
        db_email = db.query(User).filter(User.email == user.email).first()
        user_password = db_email.password

        if verify_password(user.password,user_password):

            access_token = Authorize.create_access_token(subject=db_email.email, expires_time= 30)#default algo HS256
            refresh_token = Authorize.create_refresh_token(subject=db_email.email, expires_time= 60*24*7)

            response = {"access":access_token,"refresh":refresh_token}

            return jsonable_encoder(response)

        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="wrong email and password 😢")
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="please login")


# Create refresh token
@user_routes.get('/refresh')
async def refresh_token(user : LoginUser,Authorize : AuthJWT = Depends(get_config), db : Session = Depends(get_db)):
    user_email = db.query(User).filter(User.email == user.email).first()
    db_email= user_email.email
    user_password = db_email.password
    if verify_password(user.password,user_password):

        try:
            Authorize.jwt_refresh_token_required()
        except :
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid refresh Token 😢")
    
        new_access_token = Authorize.create_access_token(subject=db_email, expires_time=30)
        new_refresh_token = Authorize.create_refresh_token(subject=db_email, expires_time=60*24*7)

        return jsonable_encoder({"new_access_token":new_access_token, "new_refresh_token":new_refresh_token})

    raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="wrong email and password 😢")
    