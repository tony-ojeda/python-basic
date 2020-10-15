def run():
    count = 0
    LIMITE = 1000
    potencia = 2**count
    while potencia < LIMITE:
        count += 1
        potencia = 2**count
        print(str(count)+" a la potencia 2 es: "+str(potencia))


if __name__ == '__main__':
    run()