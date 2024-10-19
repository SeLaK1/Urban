import unittest
import M12N2
import M12N1

programTest = unittest.TestSuite()

programTest.addTest(unittest.TestLoader().loadTestsFromTestCase(M12N1.RunnerTest))
programTest.addTest(unittest.TestLoader().loadTestsFromTestCase(M12N2.TournmentTest))

proverka = unittest.TextTestRunner(verbosity=2)
proverka.run(programTest)
