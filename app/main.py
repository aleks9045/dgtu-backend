from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.routers import fastapi_users, auth_backend
from app.auth.schemas import UserRead, UserCreate, UserUpdate
from app.publication.routers import router as publ_router

app = FastAPI(title="Swagger UI")

origins = [
    "http://127.0.0.1"
]  # Сервера, которые могут отправлять запросы на Backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Access-Control-Allow-Origin",
                   "Access-Control-Allow-Methods", "X-Requested-With",
                   "Authorization", "X-CSRF-Token"]
)  # Побеждаем политику CORS

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
    publ_router
)
