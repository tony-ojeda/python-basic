import unittest
import supercalculadora
import ut_calculadora
import expr_aritmetica

class TestsSupercalculadora(unittest.TestCase):
    def test_sumar(self):
        sc = supercalculadora.Supercalculadora(
                expr_aritmetica.ExprAritmetica())
        self.failUnlessEqual("4", sc.calcular("2 + 2"))

    def test_restar(self): 
        sc = supercalculadora.Supercalculadora(
                expr_aritmetica.ExprAritmetica())
        self.failUnlessEqual("0", sc.calcular("2 - 2"))
    
    def test_expresion_compleja_sin_parentesis_sin_precendencia(self):
        sc = supercalculadora.Supercalculadora(
                expr_artimetica.ExpreAritmetica())
        self.failUnlessEqual("6", sc.calcular("5 + 4 - 3"))

