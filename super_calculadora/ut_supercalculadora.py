import unittest
import supercalculadora

class TestsSupercalculadora(unittest.TestCase):
    
    def test_sumar_2_y_2(self):
        calc = supercalculadora.Supercalculadora()
        self.assertEqual(4, calc.sumar(2,2))
    
    def test_sumar_5_y_7(self):
        calc = supercalculadora.Supercalculadora()
        self.assertEqual(12, calc.sumar(5,7))

if __name__ == "__main__":
    unittest.main()