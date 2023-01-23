from fastapi_jwt_auth import AuthJWT
from app.user.schemas import Setting


@AuthJWT.load_config
def get_config():
    return Setting()