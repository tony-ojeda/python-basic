def exchanges(moneda,cantidad):
    result = 0
    # Moneda Peruana
    if moneda == 1:
        result = round(cantidad * 0.28,2)
        print(f'los {cantidad} soles peruanos equivalen a {result} dolares')
    # Moneda colombiana
    elif moneda == 2:
        result = round(cantidad * 0.0013,2)
        print(f'Los {cantidad} pesos chilenos equivalen a {result} dolares')
    # Moneda Argentina
    elif moneda == 3:
        result = round(cantidad * 0.014,2)
        print(f'Los {cantidad} pesos argentinos equivalen a {result} dolares')
    # Moneda Mexicana
    elif moneda == 4:
        result = round(cantidad * 0.044,2)
        print(f'Los {cantidad} pesos mexicanos equivalen a {result} dolares')
    else:
        print('Ingrese solo un número de la lista')

def logica():
    punto_salida = 0
    while True:
        try:
            while True:
                moneda = int(input('''
                Ingrese el indice de la moneda que quieres convertir a dolar:
                    [1] Moneda Peruana a Dolar
                    [2] Moneda Chilena a Dolar
                    [3] Moneda Argentina a Dolar
                    [4] Moneda Mexicana a Dolar
                    [0] Salir
                Selecciona: 
                '''))
                print('¨*******************************************')
                if(moneda >= 0 and moneda <= 4):
                    break
            if(moneda == 0):
                print('Bay bay')
                punto_salida = 1
            else:
                cantidad = int(input('Ingrese la cantidad que quieres convertir: '))
                exchanges(moneda,cantidad)
        except:
            print('Por favor, Ingrese solo valores numericos')
        if(punto_salida == 1):
            break

if __name__ == '__main__':
    try:
        logica()
    except:
        logica()
