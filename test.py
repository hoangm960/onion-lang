from io import StringIO
from src.interpreter import Interpreter
from src.parser import Parser
import unittest
import sys


class TestOnionLanguage(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def capture_output(self, code: str):
        """
        Helper to parse the given Onion code, run the visitor,
        and capture printed output along with the visitor's return value.
        """
        # Lexing & parsing

        parser = Parser()
        tree = parser.parse_input(code)
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        if tree:
            try:
                result = self.interpreter.visit(tree)
                output = sys.stdout.getvalue().strip()
                return result, output
            finally:
                sys.stdout = old_stdout

    def assertOnionOutput(self, code, expected_lines):
        _, output = self.capture_output(code)
        actual_lines = output.strip().split('\n')
        self.assertEqual(actual_lines, expected_lines)

    def test_arithmetic(self):
        code = """
        (print (+ 1 2 3))
        (print (- 10 4))
        (print (* 2 3 4))
        (print (/ 20 5))
        """
        self.assertOnionOutput(code, ["6", "6", "24", "4.0"])

    def test_booleans(self):
        code = """
        (print (== 5 5))
        (print (!= 5 3))
        (print (< 2 3))
        (print (>= 7 7))
        (print (not false))
        """
        self.assertOnionOutput(code, ["True", "True", "True", "True", "True"])

    def test_assignment_and_inc_dec(self):
        code = """
        (let x 10)
        (inc x)
        (print x)
        (dec x)
        (print x)
        """
        self.assertOnionOutput(code, ["11", "10"])

    def test_lists(self):
        code = """
        (let lst (list 1 2 3 4))
        (print (head lst))
        (print (tail lst))
        (print (getid 2 lst))
        (print (sizeof lst))
        """
        self.assertOnionOutput(code, ["1", "[2, 3, 4]", "3", "4"])

    def test_plain_if_true(self):
        code = """
        (if (> 2 1) (print "A"))
        """
        self.assertOnionOutput(code, ['A'])

    def test_plain_if_false(self):
        code = """
        (if (< 2 1) (print "A"))
        """
        self.assertOnionOutput(code, [''])

    def test_if_elif_else(self):
        code = '''
        (if (== 1 2)
            (print "A")
            (elif (> 2 1) (print "B"))
            (else (print "C"))
        )
        '''
        self.assertOnionOutput(code, ['B'])

    def test_if_else_only(self):
        code = '''
        (if false
            (print "no")
            (else (print "yes"))
        )
        '''
        self.assertOnionOutput(code, ['yes'])

    def test_if_elif_only(self):
        code = '''
        (if false
            (print "first")
            (elif false (print "second"))
            (elif true  (print "third"))
        )
        '''
        self.assertOnionOutput(code, ['third'])

    def test_cond(self):
        code = """
        (cond
            ((< 1 0)
                (print "branch1")
            )
            ((> 2 3)
                (print "branch2")
            )
            (t
                (print "default")
            )
        )
        """
        self.assertOnionOutput(code, ["default"])

    def test_loops(self):
        code = """
        (let i 0)
        (while (< i 3)
            (print i)
            (inc i)
        )
        (let count 0)
        (repeat 4
            (inc count)
        )
        (print count)
        """
        self.assertOnionOutput(code, ["0", "1", "2", "4"])

    def test_functions(self):
        code = """
        (def add (a b)
            (return (+ a b))
        )
        (print (add 2 3))

        (def fact (n)
            (if (<= n 1)
                (return 1)
                (else (return (* n (fact (- n 1)))))
            )
        )
        (print (fact 5))
        """
        self.assertOnionOutput(code, ["5", "120"])

    def test_macros(self):
        code = """
        (macro double (x)
            (print (* x 2))
        )
        (double 7)
        """
        self.assertOnionOutput(code, ["14"])


if __name__ == "__main__":
    unittest.main()
