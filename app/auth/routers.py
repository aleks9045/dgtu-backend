from fastapi_users import FastAPIUsers

from app.auth.base_config import auth_backend
from app.auth.manager import get_user_manager
from database import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
