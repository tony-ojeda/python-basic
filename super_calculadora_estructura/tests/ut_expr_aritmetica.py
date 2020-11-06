import unittest
from expr_aritmetica import ExprAritmetica

class TestsExpAritmetica(unittest.TestCase):
    
    def test_extraer_operandos_y_operadores_en_2_mas_2(self):
        expresion = ExprAritmetica()
        self.failUnless({'Operandos':[2,2],'Operadores':['+']},expresion.parse("2 + 2"))