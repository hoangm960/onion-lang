from io import StringIO
from src.interpreter import Interpreter
from src.parser import Parser
import unittest
import sys
import os

TEST_DIR = "./tests/semantics"


class FileTestCase(unittest.TestCase):
    def __init__(self, file_path) -> None:
        super().__init__()
        self.file_path = file_path

    def __str__(self) -> str:
        return f"{self.__class__.__name__}:{os.path.basename(self.file_path)}"


class SemanticTest(FileTestCase):
    def capture_output(self, code: str):
        parser = Parser()
        tree = parser.parse_input(code)
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        if tree:
            try:
                result = self.interpreter.visit(tree)
                output = sys.stdout.getvalue().strip()
                return output
            finally:
                sys.stdout = old_stdout
        return None

    def assertOutput(self, code, expected_lines):
        filename = os.path.basename(self.file_path)
        OUTPUT_DIR = os.path.join(
            TEST_DIR,
            "output",
        )
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, filename)

        output = self.capture_output(code)
        if not output is None:
            output = output.strip()
            with open(OUTPUT_FILE_PATH, "w") as fout:
                fout.write(output)
            self.assertEqual(output, expected_lines.strip())
        else:
            self.fail("No output")

    def setUp(self):
        self.interpreter = Interpreter()

    def runTest(self):
        test_data = None
        with open(self.file_path) as fin:
            test_data = fin.read()

        if not test_data:
            raise Exception("File empty")
        code, expectedOutput = test_data.split("\n\n")
        self.assertOutput(code, expectedOutput)


def get_suite():
    suite = unittest.TestSuite()
    INPUT_FILE_PATH = os.path.join(TEST_DIR, "input")

    for file in os.listdir(INPUT_FILE_PATH):
        file_path = os.path.join(INPUT_FILE_PATH, file)

        if file.endswith(".onion"):
            suite.addTest(SemanticTest(file_path))

    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(get_suite())
