import unitest
import unittest

class RunnerTest(unittest.TestCase):
    runner1 = unitest.Runner('Sergio')
    runner2 = unitest.Runner('Banana')
    def test_walk(self):
        for _ in range(10):
            self.runner1.walk()
        self.assertEqual(self.runner1.distance, 50)

    def test_run(self):
        for _ in range(10):
            self.runner2.run()
        self.assertEqual(self.runner2.distance, 100)

    def test_sravnenie(self):
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)


if __name__ == '__main__':
    unittest.main()