import os
from dotenv import load_dotenv # !pip install dotenv

print("Hola mundo")

def saludar():
    print("Hola :D")

clave_super_secreta = os.getenv("llave_api_super_secreta")