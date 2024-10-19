from pprint import pprint
import unitest2
import unittest

class TournmentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def ttearDownClass(self):
        rez = {}
        for key in self.all_results:
            rez[key] = self.all_results[key].name
        print(rez)

    def setUp(self):
        self.r1 = unitest2.Runner('Усэйн', 10)
        self.r2 = unitest2.Runner('Андрей', 9)
        self.r3 = unitest2.Runner('Ник', 4)

    def TournamentTest(self, *partisipants):
        t1 = unitest2.Tournament(90, *partisipants)
        self.all_results = t1.start()
        for key1 in self.all_results:
            for key2 in self.all_results:
                if key1 < key2:
                    if self.all_results[key2].speed > self.all_results[key1].speed:
                       perem = self.all_results[key1]
                       self.all_results[key1] = self.all_results[key2]
                       self.all_results[key2] = perem
        return self.all_results

    @unittest.skipIf(is_frozen, 'В данном классе все тесты заморожены')
    def test_True_First(self):
        self.assertEqual(self.TournamentTest(self.r1, self.r3)[self.all_results.__len__()].name, 'Ник')
        self.ttearDownClass()

    @unittest.skipIf(is_frozen, 'В данном классе все тесты заморожены')
    def test_True_Second(self):
        self.assertEqual(self.TournamentTest(self.r3, self.r2)[self.all_results.__len__()].name, 'Ник')
        self.ttearDownClass()

    @unittest.skipIf(is_frozen, 'В данном классе все тесты заморожены')
    def test_True_Third(self):
        self.assertEqual(self.TournamentTest(self.r1, self.r2, self.r3)[self.all_results.__len__()].name, 'Ник')
        self.ttearDownClass()

if __name__ == '__main__':
    unittest.main()



