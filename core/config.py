from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_ECHO: bool

    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int

    PRIVATE_KEY_PATH: Path = BASE_DIR / "certs" / "jwt-private.pem"
    PUBLIC_KEY_PATH: Path = BASE_DIR / "certs" / "jwt-public.pem"

    LIFETIME_SECONDS: int
    RESET_PASSWORD_SECRET: str
    VERIFICATION_PASSWORD_SECRET: str

    SUPER_USER_EMAIL: str
    SUPER_USER_PASSWORD: str

    model_config = SettingsConfigDict(env_file='.env')

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def database_echo(self):
        return self.DB_ECHO

    @property
    def jwt_settings(self):
        return {
            "algorithm": self.JWT_ALGORITHM,
            "access_token_expire_minutes": self.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
            "refresh_token_expire_days": self.JWT_REFRESH_TOKEN_EXPIRE_DAYS,
            "private_key_path": self.PRIVATE_KEY_PATH,
            "public_key_path": self.PUBLIC_KEY_PATH
        }

    @property
    def jwt_database_settings(self):
        return {
            "token_lifetime_seconds": self.LIFETIME_SECONDS,
            "reset_password_secret": self.RESET_PASSWORD_SECRET,
            "verification_password_secret": self.VERIFICATION_PASSWORD_SECRET
        }

    @property
    def super_user(self):
        return {
            "super_user_email": self.SUPER_USER_EMAIL,
            "super_user_password": self.SUPER_USER_PASSWORD
        }


settings = Settings()
