import unittest
import ut_calculadora
import ut_expr_aritmetica
import ut_supercalculadora

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite( ut_calculadora.TestsCalculadora ))
    suite.addTest(unittest.makeSuite( ut_expr_aritmetica.TestsExpAritmetica ))
    suite.addTest(unittest.makeSuite( ut_supercalculadora.TestsSupercalculadora ))
    unittest.TextTestRunner(verbosity=3).run(suite)
