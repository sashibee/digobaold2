import jwt
from ninja.security import HttpBearer
from decouple import config

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            #JWT secret key is set up in settings.py
            JWT_SIGNING_KEY = config("JWT_SIGNING_KEY", default=None)
            payload = jwt.decode(token, JWT_SIGNING_KEY, algorithms=["HS256"])
            username: str = payload.get("sub")
            if username is None:
                return None
        except jwt.PyJWTError as e:
            return None
        return username

def create_token(username):
    JWT_SIGNING_KEY = config("JWT_SIGNING_KEY", default=None)
    JWT_ACCESS_EXPIRY = config("JWT_ACCESS_EXPIRY", default = "15") # 15 minutes expiration
    to_encode_access = {"sub": username}
    access_expire = datetime.utcnow() + timedelta(minutes=JWT_ACCESS_EXPIRY)
    to_encode_access.update({"exp": access_expire})
    encoded_access_jwt = jwt.encode(to_encode_access, JWT_SIGNING_KEY, algorithm="HS256")
    return encoded_access_jwt


# from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import check_password
# from ninja.errors import ValidationError

# class TokenSchema(Schema):
#     access: str

# @router.post(
#     "/sign_in",
#     auth=None,
#     response={200: TokenSchema},
# )
# def sign_in(request, username: str = Form(...), password: str = Form(...)):
#     try:
#         user_model = get_user_model().objects.get(username=username)
#     except get_user_model().DoesNotExist:
#         raise ValidationError

#     passwords_match = check_password(password, user_model.password)
#     if not passwords_match:
#         raise ValidationError
    
#     access = create_token(user_model.username)
#     return 200, TokenSchema(access=access)


