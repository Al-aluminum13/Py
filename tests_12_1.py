class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def walk(self):
        self.distance += 5

    def run(self):
        self.distance += 10

import unittest

class RunnerTest(unittest.TestCase):
    
    def test_walk(self):
        runner = Runner("TestWalker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("TestWalker")
        runner2 = Runner("TestRunner")
        
        for _ in range(10):
            runner1.walk()
            runner2.run()
        
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()

