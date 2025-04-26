import sys
import os

# Add project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.parser import Parser
from src.interpreter import Interpreter


# Test comment handling
if __name__ == "__main__":
    parser = Parser()
    interpreter = Interpreter()
    
    # Ví dụ mã Onion với comment
    sample_code = """
    (let x 5) // Gán x = 5
    (print (+ x 3))   // Print the result of adding x and 3
    """
    
    tree = parser.parse_input(sample_code)
    if tree:
        print("Cây cú pháp:")
        print(parser.get_str_tree())
        
        print("\nKết quả thực thi:")
        result = interpreter.visit(tree)
        print("Kết quả cuối cùng:", result)
    else:
        print("Phân tích không thành công.") 