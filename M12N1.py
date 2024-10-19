import unitest1
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    runner1 = unitest1.Runner('Sergio')
    runner2 = unitest1.Runner('Banana')

    @unittest.skipIf(is_frozen, 'Данный тест заморожен')
    def test_walk(self):
        for _ in range(10):
            self.runner1.walk()
        self.assertEqual(self.runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Данный тест заморожен')
    def test_run(self):
        for _ in range(10):
            self.runner2.run()
        self.assertEqual(self.runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Данный тест заморожен')
    def test_sravnenie(self):
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)


if __name__ == '__main__':
    unittest.main()
