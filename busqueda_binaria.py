objetivo = int(input('Escoge un numero. '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2
# Este es un comentario de prueba
while abs(respuestas**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, repuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2
print(f'La raiz cuadrada de {objetivo} es {respuesta}')