import unittest
from super_calculadora.tests.ut_calculadora import TestsCalculadora
# from ut_expr_aritmetica import TestsExpAritmetica

if __name__ == "__main__":
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite( TestsCalculadora ))
    # suite.addTest(unittest.makeSuite( ut_expr_aritmetica.TestsExprAritmetica ))
    # unittest.TextTestRunner(verbosity=3).run(suite)