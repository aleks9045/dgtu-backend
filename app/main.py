from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.schemas import UserRead, UserCreate, UserUpdate
from app.auth.routers import fastapi_users, auth_backend
from app.articles.routers import router as articles_router

app = FastAPI(title='My app')

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Access-Control-Allow-Origin", "Access-Control-Allow-Methods", "Set-cookie"]
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    articles_router,
)
