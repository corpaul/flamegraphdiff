import unittest
from graphs.diff_flame_graphs import DiffFlameGraph


class TestPerformanceFunctions(unittest.TestCase):

    def testEqual(self):
        diff = DiffFlameGraph()
        compare = {"a;b;c": 50, "a;b": int(-50)}
        compare2 = {"a;b;c": 50, "a;b": int(-50)}
        compare3 = {"a;b;c": 10, "a;b": int(-50)}
        compare4 = {"a;": 50, "a;b": int(-50)}
        self.assertTrue(diff.equal(compare, compare2))
        self.assertFalse(diff.equal(compare, compare3))
        self.assertFalse(diff.equal(compare, compare4))

    def testDiffKeys(self):
        diff = DiffFlameGraph()
        val1 = diff.loadCSV("testa.txt")
        val2 = diff.loadCSV("testb.txt")

        diffCsv = diff.diffCsv(val1, val2)

        # a;b; is gone from version 2 so should be -50
        # a;b;c is new, so should be 50
        compare = {"a;b;c": 50, "a;b": int(-50)}
        self.assertTrue(diff.equal(diffCsv, compare))

    def testWriteDiff(self):
        diff = DiffFlameGraph()
        val1 = diff.loadCSV("testa.txt")
        val2 = diff.loadCSV("testb.txt")

        diffCsv = diff.diffCsv(val1, val2)
        diff.writeDiff(diffCsv, "../output/diff.txt")

        diffCsv2 = diff.loadCSV("../output/diff.txt")
        self.assertTrue(diff.equal(diffCsv, diffCsv2))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
