import logging

import unitest2
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    runner1 = unitest2.Runner('Sergio', -3)
    runner2 = unitest2.Runner(True, 5)

    @unittest.skipIf(is_frozen, 'Данный тест заморожен')
    def test_walk(self):
        try:
            if self.runner1.speed >= 0:
                for _ in range(10):
                    self.runner1.walk()
                self.assertEqual(self.runner1.distance, 50)
                logging.info(f'test_walk выполнен успешно')
            else: raise TypeError
        except TypeError:
            logging.warning('Неверная скорость для runner1')


    @unittest.skipIf(is_frozen, 'Данный тест заморожен')
    def test_run(self):
        try:
            if isinstance(self.runner2.name, str):
                for _ in range(10):
                    self.runner2.run()
                self.assertEqual(self.runner2.distance, 100)
                logging.info(f'test_run выполнен успешно')
            else: raise TypeError
        except TypeError:
            logging.warning(f'Неверный тип имени для объекта runner2')

    @unittest.skip
    def test_sravnenie(self):
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF8', format='%(asctime)s | %(levelnames)s | %(message)s')

    RunnerTest.test_run()