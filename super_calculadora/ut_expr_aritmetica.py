import unittest
import expr_aritmetica

class TestsExpAritmetica(unittest.TestCase):
    def setUp(self):
        self.expresion = expr_aritmetica.ExprAritmetica()
    
    def tearDown(self):
        pass
    
    def test_extraer_operandos_y_operadores_en_2_mas_2(self):
        self.failUnless({'operandos':[2,2],'operadores':['+']},self.expresion.parse("2 + 2"))
    
    def test_extraer_operandos_y_operadores_en_10_entre_menos_5(self):
        self.assertEqual({'operandos':[10, -5], 'operadores':['/']}, self.expresion.parse("10 / -5"))

    def test_extraer_operandos_y_operadores_expr_sin_parentesis(self):
        self.failUnlessEqual({'operandos':[5,4,2,2], 'operadores':['+','*','/']},
        self.expresion.parse("5 + 4 * 2 / 2"))
