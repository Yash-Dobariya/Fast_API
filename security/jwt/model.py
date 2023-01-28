from sqlalchemy import Column, Integer, String

class User_db:

    __table__ = "user"

    username = Column(String)
    password = Column(String)
    full_name = Column(String)
    email = Column(String)

# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
