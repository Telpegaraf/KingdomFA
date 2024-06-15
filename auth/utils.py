import bcrypt
from datetime import datetime, timedelta
import jwt
from core.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.jwt_settings.get("private_key_path").read_text(),
    algorithm: str = settings.jwt_settings.get("algorithm"),
    expire_minutes: int = settings.jwt_settings.get("access_token_expire_minutes"),
    expire_timedelta: timedelta | None = None,
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = expire_timedelta + now
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.jwt_settings.get("public_key_path").read_text(),
    algorithms: str = settings.jwt_settings.get("algorithm")
):
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithms]
    )
    return decoded


def hash_password(password):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    string_password = hashed_password.decode('utf8')
    return string_password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


a = "admin"

a1 = hash_password(a)

print(type(a1),a1)

b = "admin"
b = b.encode('utf-8')
b = b.decode('utf-8')

print(verify_password(b, a1))
