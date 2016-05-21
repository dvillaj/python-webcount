from unittest import TestCase
from matheval.evaluator import math_eval

class EvaluatorTest(TestCase):
    def _check(self, tree, expected):
        self.assertEqual(math_eval(tree), expected)

    def test_basic(self):
        self._check(5, 5)
        self._check(['+', 5], 5)
        self._check(['+', 5, 7], 12)
        self._check(['*', ['+', 5, 4], 2], 18)
        
