from jwt import encode, decode

""" Crear token """
def create_token(data: dict):
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

""" Validar Token """
def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithm=['HS256'])
    return data