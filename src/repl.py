from src.interpreter import Interpreter
from src.parser import Parser
from generated.OnionParser import OnionParser
import os
import glob


def run_onion_file(filename, interpreter, save_output=False):
    """Thực thi tệp Onion với đường dẫn đã cho"""
    try:
        # Chuẩn hóa đường dẫn tệp
        if not os.path.isabs(filename):
            # Thử các đường dẫn tương đối khác nhau
            if os.path.exists(filename):
                pass  # Sử dụng đường dẫn như đã nhập
            elif os.path.exists(os.path.join('tests', 'parsers', 'input', filename)):
                filename = os.path.join('tests', 'parsers', 'input', filename)
            else:
                # Thêm đuôi .onion nếu không có
                if not filename.endswith('.onion'):
                    if os.path.exists(filename + '.onion'):
                        filename = filename + '.onion'
                    elif os.path.exists(os.path.join('tests', 'parsers', 'input', filename + '.onion')):
                        filename = os.path.join('tests', 'parsers', 'input', filename + '.onion')
        
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found")
            return None
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Không in thông báo chạy file
        parser = Parser()
        tree = parser.parse_input(content)
        
        if tree:
            # Lưu trữ output nếu cần thiết
            original_stdout = None
            output_file = None
            
            if save_output:
                # Tạo thư mục output nếu không tồn tại
                output_dir = os.path.join('tests', 'parsers', 'output')
                os.makedirs(output_dir, exist_ok=True)
                
                # Tạo tên tệp output
                base_filename = os.path.basename(filename)
                output_filename = os.path.join(output_dir, base_filename)
                
                # Mở tệp output
                output_file = open(output_filename, 'w', encoding='utf-8')
                print(f"Saving output to: {output_filename}")
                
                # Lưu kết quả phân tích cú pháp
                output_file.write(f"# Syntax Tree for {base_filename}\n")
                output_file.write(parser.get_str_tree())
                output_file.write("\n\n# Execution Results\n")
            
            # Thực thi mã
            result = interpreter.visit(tree)
            
            if save_output and output_file:
                # Lưu kết quả thực thi
                output_file.write(f"Final result: {result}\n")
                output_file.close()
            
            # Chỉ in kết quả cuối cùng nếu không phải là hàm main và có giá trị khác None
            # Kiểm tra nếu chương trình kết thúc bằng việc gọi hàm main
            has_main_call = False
            for i in range(tree.getChildCount()):
                if tree.getChild(i).getText().strip() == "(main)":
                    has_main_call = True
                    break
            
            if result is not None and not has_main_call:
                print(f"{result}")
                
            # Không in thông báo hoàn thành việc thực thi
            return result
        else:
            print("Failed to parse the file")
            return None
    except Exception as e:
        print(f"Error running file: {e}")
        return None


def run_all_files(interpreter):
    """Thực thi tất cả các tệp .onion trong thư mục tests/parsers/input"""
    try:
        input_dir = os.path.join('tests', 'input')
        if not os.path.exists(input_dir):
            print(f"Error: Directory '{input_dir}' not found")
            return
        
        onion_files = glob.glob(os.path.join(input_dir, '*.onion'))
        if not onion_files:
            print(f"No .onion files found in {input_dir}")
            return
        
        print(f"Running {len(onion_files)} files...")
        for file in onion_files:
            print("\n" + "="*50)
            run_onion_file(file, interpreter, save_output=True)
        
        print("\n" + "="*50)
        print(f"All {len(onion_files)} files executed and outputs saved to tests/parsers/output/")
    except Exception as e:
        print(f"Error running all files: {e}")


def clear_screen():
    """Xóa màn hình terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_help():
    """Hiển thị hướng dẫn sử dụng REPL"""
    help_text = """
ONION REPL COMMANDS:
-------------------
- run <filename>       : Run a specific Onion file
                         (can be relative or absolute path)
                         Example: run arithmetic.onion
                         
- run <filename> -s    : Run a file and save output to tests/parsers/output/
- run <filename> --save: Same as above

- runall               : Run all .onion files in tests/parsers/input directory
                         and save outputs to tests/parsers/output/
                        
- clear                : Clear the terminal screen
                        
- help                 : Show this help message

- exit, quit           : Exit the REPL

CODE EXAMPLES:
------------
- Variable assignment  : (let x 5)
- Arithmetic           : (+ x 3)
- Print                : (print x)
- List                 : (list 1 2 3)
- List operations      : (head arr), (tail arr)
- Comments             : // This is a comment
"""
    print(help_text)


def run_file(filename):
    """Hàm helper để chạy tệp Onion và handle exception."""
    try:
        interpreter = Interpreter()
        return run_onion_file(filename, interpreter)
    except Exception as e:
        print(f"Error running file: {e}")
        return None


def main():
    interpreter = Interpreter()
    print("🧅 Onion REPL - type 'exit' or Ctrl+C to quit")
    print("Type 'help' for available commands")
    while True:
        try:
            line = input(">>> ").strip()
            tokens = line.split()
            
            if line.strip().lower() in ('exit', 'quit'):
                break
            elif line == "":
                continue
            elif line.lower() == "help":
                show_help()
            elif line.lower() == "clear":
                clear_screen()
            elif line.lower().startswith("run "):
                # Lệnh chạy tệp Onion
                parts = line[4:].strip().split()
                
                # Kiểm tra tùy chọn lưu output
                save_output = False
                if len(parts) >= 2 and parts[-1] in ('-s', '--save'):
                    save_output = True
                    filename = ' '.join(parts[:-1])
                else:
                    filename = ' '.join(parts)
                
                run_onion_file(filename, interpreter, save_output)
            elif line.lower() == "runall":
                # Lệnh chạy tất cả các tệp
                run_all_files(interpreter)
            else:
                # Kiểm tra nếu đây là câu lệnh assignment bằng cách đơn giản
                is_assignment = False
                is_print = False
                
                if line.startswith("(let "):
                    is_assignment = True
                elif line.startswith("(print "):
                    is_print = True
                
                parser = Parser()
                tree = parser.parse_input(line)
                if tree:
                    result = interpreter.visit(tree)
                    
                    # Chỉ in kết quả nếu không phải assignment và không phải print
                    # và không phải hàm không có giá trị trả về
                    if result is not None and not is_assignment and not is_print:
                        print(f"Result: {result}")
        except KeyboardInterrupt:
            print("\nBye!")
            break
        except Exception as e:
            print(f"Error: {e}")
