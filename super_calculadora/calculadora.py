class Calculadora:
    
    def __init__(self):
        print('Clase calculadora creada')
    
    def sumar(self,a,b):
        return a + b
    
    def restar(self,a,b):
        return a - b

    def dividir(self,a,b):
        if a % b != 0:
            raise ValueError
        else:
            return a / b