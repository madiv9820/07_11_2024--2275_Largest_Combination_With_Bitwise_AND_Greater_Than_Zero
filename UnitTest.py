from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([16,17,71,62,12,24,14], 4), 2: ([8,8], 2)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        candidates, output = self.__testCases[1]
        result = self.__obj.largestCombination(candidates = candidates)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        candidates, output = self.__testCases[2]
        result = self.__obj.largestCombination(candidates = candidates)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__== '__main__': unittest.main()