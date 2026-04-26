import os
from dotenv import load_dotenv # !pip install dotenv

print("Hola mundo")

def saludar():
    print("Hola :D")

def saludo_pregunta():
    print("Hola ¿cómo estás?")

clave_super_secreta = os.getenv("llave_api_super_secreta")