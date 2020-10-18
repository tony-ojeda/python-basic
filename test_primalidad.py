def es_primo(numero):
    if numero == 1: return False
    contador = 0
    for i in range(1,numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    # if continue == 0
    #     return True
    # else 
    #     return False
    return True if contador == 0 else False
    
def run():
    numero = int(input('Escribe un número:'))
    if es_primo(numero):
        print('Es numero primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()