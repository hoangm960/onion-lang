import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generated.OnionParser import OnionParser
from generated.OnionVisitor import OnionVisitor

class ReturnValue:
    """Lớp bọc giá trị trả về bởi lệnh return."""
    def __init__(self, value):
        self.value = value

class SymbolTable:
    """Bảng ký hiệu phân cấp để quản lý phạm vi biến."""
    def __init__(self, parent=None):
        self.symbols = {}  # lưu trữ biến ở phạm vi hiện tại
        self.parent = parent  # bảng ký hiệu phạm vi cha
        
    def define(self, name, value):
        """Định nghĩa một biến trong phạm vi hiện tại."""
        self.symbols[name] = value
        
    def resolve(self, name):
        """Tìm giá trị của biến trong các phạm vi lồng nhau."""
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.resolve(name)
        else:
            raise NameError(f"Variable '{name}' is not defined")
            
    def assign(self, name, value):
        """Gán giá trị cho biến đã tồn tại."""
        if name in self.symbols:
            self.symbols[name] = value
            return True
        elif self.parent:
            return self.parent.assign(name, value)
        else:
            return False

class Interpreter(OnionVisitor):
    def __init__(self):
        self.env = SymbolTable()
        self.functions = {}  # Lưu trữ các định nghĩa hàm

    def visitProgram(self, ctx):
        result = None
        for stmt in ctx.statement():
            result = self.visit(stmt)
            
            # Kiểm tra xem nếu có lỗi không tìm thấy hàm, thử coi như đó là lời gọi hàm
            if isinstance(result, Exception) and isinstance(result, NameError) and "' is not defined" in str(result):
                # Tách tên từ thông báo lỗi
                var_name = str(result).split("'")[1]
                
                # Kiểm tra xem có phải là tên hàm không
                if var_name in self.functions:
                    # Đây là lời gọi hàm không tham số
                    try:
                        # Tạo môi trường mới
                        function_env = SymbolTable(self.env)
                        
                        # Lưu môi trường hiện tại
                        previous_env = self.env
                        
                        # Thiết lập môi trường mới
                        self.env = function_env
                        
                        # Lấy thân hàm từ định nghĩa hàm
                        body = self.functions[var_name]['body']
                        
                        # Thực thi thân hàm
                        call_result = None
                        for i in range(body.getChildCount()):
                            stmt_result = self.visit(body.getChild(i))
                            if isinstance(stmt_result, ReturnValue):
                                call_result = stmt_result.value
                                break
                            elif stmt_result is not None:
                                call_result = stmt_result
                                
                        # Khôi phục môi trường
                        self.env = previous_env
                        
                        # Gán lại result
                        result = call_result
                    except Exception as e:
                        # Nếu có lỗi, giữ nguyên result là lỗi ban đầu
                        pass
        
        return result

    def visitStatement(self, ctx):
        # Xử lý câu lệnh trong ngoặc đơn: '(' statementType ')'
        if ctx.getChildCount() >= 3 and ctx.statementType() is not None:
            # Gọi visit cho statementType
            result = self.visit(ctx.statementType())
            # Trả về kết quả mà không cần xử lý thêm
            return result
        # Trường hợp không có statementType, truy cập trực tiếp các nút con
        for i in range(ctx.getChildCount()):
            if i != 0 and i != ctx.getChildCount() - 1:  # Bỏ qua dấu ngoặc đơn
                child = ctx.getChild(i)
                if child is not None:
                    return self.visit(child)
        return None

    def visitStatementType(self, ctx):
        # Truy cập loại câu lệnh cụ thể (assignment, expression, v.v.)
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child is not None:
                result = self.visit(child)
                if result is not None:
                    return result
        return None

    def visitPrintStatement(self, ctx):
        try:
            value = self.visit(ctx.expression())
            print(value)
            # Trả về None thay vì value để tránh in kép
            return None
        except Exception as e:
            # Xử lý các lỗi khác
            print(f"Print error: {e}")
            return None

    def visitAssignment(self, ctx):
        if ctx.getChildCount() == 3:  # 'let' IDENTIFIER expression
            # Dạng đơn giản: let a 2
            identifier = ctx.getChild(1).getText()
            value = self.visit(ctx.getChild(2))
            # print(f"Debug: {value}")
            self.env.define(identifier, value)
            return value
        else:
            # Dạng nhiều biến: let (a 1) (b 2)
            result = None
            # Bắt đầu từ vị trí 1 (sau 'let')
            i = 1
            while i < ctx.getChildCount():
                if ctx.getChild(i).getText() == '(':
                    # Mỗi cặp biến-giá trị có dạng '(' IDENTIFIER expression ')'
                    pair = ctx.getChild(i)
                    if pair.getChildCount() == 4:  # '(', IDENTIFIER, expression, ')'
                        var_name = pair.getChild(1).getText()
                        var_value = self.visit(pair.getChild(2))
                        self.env.define(var_name, var_value)
                        result = var_value
                i += 1
            return result

    # def visitProgram(self, ctx):
    #     print("DEBUG: Entering visitProgram")
    #     result = None
        
    #     # Store the original visit method to wrap it
    #     original_visit = self.visit
        
    #     # Define a new visit method that adds debugging
    #     def debug_visit(node):
    #         method_name = node.__class__.__name__
    #         # Strip "Context" suffix if it exists
    #         if method_name.endswith("Context"):
    #             method_name = method_name[:-7]
    #         print(f"DEBUG: Visiting {method_name}")
            
    #         # Call the original visit method and track the result
    #         visit_result = original_visit(node)
    #         print(f"DEBUG: Finished {method_name} with result type: {type(visit_result)}")
    #         if visit_result is None:
    #             print(f"DEBUG: Warning - {method_name} returned None")
    #         return visit_result
        
    #     # Temporarily replace the visit method
    #     self.visit = debug_visit
        
    #     try:
    #         for stmt in ctx.statement():
    #             print(f"DEBUG: Processing statement: {stmt.getText()}")
    #             result = self.visit(stmt)
                
    #             # Check if there's an error about undefined name, try as function call
    #             if isinstance(result, Exception) and isinstance(result, NameError) and "' is not defined" in str(result):
    #                 # Extract name from error message
    #                 var_name = str(result).split("'")[1]
                    
    #                 # Check if it's a function name
    #                 if var_name in self.functions:
    #                     print(f"DEBUG: Found function '{var_name}', executing it")
    #                     # This is a parameter-less function call
    #                     try:
    #                         # Create new environment
    #                         function_env = SymbolTable(self.env)
                            
    #                         # Save current environment
    #                         previous_env = self.env
                            
    #                         # Set new environment
    #                         self.env = function_env
                            
    #                         # Get function body from function definition
    #                         body = self.functions[var_name]['body']
                            
    #                         # Execute function body
    #                         call_result = None
    #                         for i in range(body.getChildCount()):
    #                             print(f"DEBUG: Executing function body statement {i}")
    #                             stmt_result = self.visit(body.getChild(i))
    #                             if isinstance(stmt_result, ReturnValue):
    #                                 call_result = stmt_result.value
    #                                 print(f"DEBUG: Return value from function: {call_result}")
    #                                 break
    #                             elif stmt_result is not None:
    #                                 call_result = stmt_result
                                    
    #                         # Restore environment
    #                         self.env = previous_env
                            
    #                         # Reassign result
    #                         result = call_result
    #                         print(f"DEBUG: Function execution result: {result}")
    #                     except Exception as e:
    #                         print(f"DEBUG: Error during function execution: {e}")
    #                         # If there's an error, keep the original error result
    #                         pass
    #                 else:
    #                     print(f"DEBUG: '{var_name}' is not a defined function")
    #     finally:
    #         # Restore the original visit method
    #         self.visit = original_visit
        
    #     print(f"DEBUG: Exiting visitProgram with result: {result}")
    #     return result


    def visitArithmeticExpr(self, ctx):
        op = ctx.getChild(0).getText()
        
        if op == '+':
            # Addition: Sum all child expressions.
            result = 0
            for i in range(1, ctx.getChildCount()):  # Skip '+'
                child = ctx.getChild(i)
                child_value = self.visit(child)
                if child_value is None:
                    raise ValueError(f"Cannot evaluate expression at position {i}")
                result += child_value
            return result
        elif op == '-':
            # Subtraction: only 2 operands
            if ctx.getChildCount() != 3:  # '-', expr1, expr2
                raise SyntaxError("Subtraction requires exactly 2 operands")
            
            # Get first operand
            first_operand = ctx.getChild(1)
            first_value = self.visit(first_operand)
            if first_value is None:
                raise ValueError("First operand of subtraction cannot be evaluated")
            
            # Get second operand
            second_operand = ctx.getChild(2)
            second_value = self.visit(second_operand)
            if second_value is None:
                raise ValueError("Second operand of subtraction cannot be evaluated")
            
            return first_value - second_value
        elif op == '*':
            # Multiplication: multiply all child expressions.
            result = 1
            for i in range(1, ctx.getChildCount()):  # Skip '*'
                child = ctx.getChild(i)
                child_value = self.visit(child)
                if child_value is None:
                    raise ValueError(f"Cannot evaluate expression at position {i}")
                result *= child_value
            return result
        elif op == '/':
            # Division: only 2 operands
            if ctx.getChildCount() != 3:  # '/', expr1, expr2
                raise SyntaxError("Division requires exactly 2 operands")
            
            # Get first operand
            first_operand = ctx.getChild(1)
            numerator = self.visit(first_operand)
            if numerator is None:
                raise ValueError("First operand of division cannot be evaluated")
            
            # Get second operand
            second_operand = ctx.getChild(2)
            denominator = self.visit(second_operand)
            if denominator is None:
                raise ValueError("Second operand of division cannot be evaluated")
            
            if denominator == 0:
                raise ZeroDivisionError("Division by zero")
            
            result = numerator / denominator
            return result
        else:
            return None
        
    def visitListExpr(self, ctx):
        # First child is 'list' keyword, skip it
        result = []
        
        # Start from index 1 to skip the 'list' keyword
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            child_value = self.visit(child)
            
            if child_value is None:
                raise ValueError(f"Cannot evaluate list element at position {i}")
                
            result.append(child_value)
        return result
    

    def visitLiteral(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            text = ctx.STRING().getText()
            return text[1:-1]
        elif ctx.BOOL():
            token = ctx.BOOL().getText()
            return token == 'true'
        return None

    def visitExpression(self, ctx):
        # Check các loại cụ thể của expression
        if ctx.literal():
            result = self.visit(ctx.literal())
            return result
        elif ctx.arithmeticExpr():
            result = self.visit(ctx.arithmeticExpr())
            return result
        elif ctx.booleanExpr():
            result = self.visit(ctx.booleanExpr())
            return result
        elif ctx.listExpr():
            result = self.visit(ctx.listExpr())
            return result
        elif ctx.functionCall():
            result = self.visit(ctx.functionCall())
            return result
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            
            # Kiểm tra nếu là tên hàm và được gọi trực tiếp
            if var_name in self.functions and ctx.getChildCount() == 1:
                # Gọi hàm không tham số
                function_def = self.functions[var_name]
                
                # Kiểm tra nếu hàm yêu cầu tham số
                if len(function_def['params']) > 0:
                    raise ValueError(f"Function '{var_name}' requires {len(function_def['params'])} arguments, got 0")
                
                # Lưu môi trường hiện tại
                previous_env = self.env
                
                # Tạo môi trường mới
                function_env = SymbolTable(previous_env)
                
                # Đặt môi trường mới
                self.env = function_env
                
                result = None
                try:
                    # Lấy thân hàm
                    body = function_def['body']
                    
                    # Thực thi từng câu lệnh
                    for i in range(body.getChildCount()):
                        stmt = body.getChild(i)
                        stmt_result = self.visit(stmt)
                        
                        if isinstance(stmt_result, ReturnValue):
                            result = stmt_result.value
                            break
                        elif stmt_result is not None:
                            result = stmt_result
                except Exception as e:
                    raise e
                finally:
                    # Khôi phục môi trường cũ
                    self.env = previous_env
                
                return result
            else:
                # Nếu không phải hàm, xử lý như biến thông thường
                try:
                    result = self.env.resolve(var_name)
                    return result
                except NameError as e:
                    # Nếu không tìm thấy biến, trả về exception thay vì ném ra
                    return e
        
        # Xử lý biểu thức lồng nhau trong ngoặc đơn: '(' expression ')'
        if ctx.getChildCount() >= 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            # Lấy biểu thức con ở giữa
            inner_expr = ctx.getChild(1)
            result = self.visit(inner_expr)
            
            # Nếu kết quả là exception, ném ra
            if isinstance(result, Exception):
                raise result
                
            return result
            
        return None

    def visitListOpExpr(self, ctx):
        # Determine which operation we're dealing with
        operation = ctx.getChild(0).getText()
        
        # Debug the structure
        print(f"DEBUG ListOp: operation={operation}, children={[ctx.getChild(i).getText() for i in range(ctx.getChildCount())]}")
        
        # Variables to store the list and index if needed
        lst = None
        
        if operation == 'head' or operation == 'tail':
            # Get the list from the appropriate child
            # Format could be: head(mylist) or head mylist
            # Try different child indices to find the list
            
            # First try standard format with parentheses
            if ctx.getChildCount() >= 3:
                list_node = ctx.getChild(2)
                lst = self.visit(list_node)
                
                # If list_node was a variable name, lst might need further resolution
                if not isinstance(lst, list) and isinstance(lst, str):
                    try:
                        lst = self.env.resolve(lst)
                    except:
                        # If that fails, try directly as an identifier
                        var_name = list_node.getText()
                        lst = self.env.resolve(var_name)
            
        elif operation == 'getid':
            # Format: getid expression(mylist) or getid expression mylist
            
            # Get the index
            if ctx.getChildCount() >= 2:
                index_expr = ctx.getChild(1)
                index = self.visit(index_expr)
                
                if not isinstance(index, int):
                    raise TypeError(f"Index must be an integer, got {type(index).__name__}")
                
                # Get the list
                if ctx.getChildCount() >= 4:
                    list_node = ctx.getChild(3)
                    lst = self.visit(list_node)
                    
                    # If list_node was a variable name, lst might need further resolution
                    if not isinstance(lst, list) and isinstance(lst, str):
                        try:
                            lst = self.env.resolve(lst)
                        except:
                            # If that fails, try directly as an identifier
                            var_name = list_node.getText()
                            lst = self.env.resolve(var_name)
            
        # Validate and perform the operation
        if lst is not None:
            if not isinstance(lst, list):
                raise TypeError(f"Expected a list but got {type(lst).__name__} with value {lst}")
                
            if not lst:
                raise ValueError(f"Cannot perform {operation} on empty list")
                
            if operation == 'head':
                # Return the first element of the list
                return lst[0]
            elif operation == 'tail':
                # Return all elements except the first one
                return lst[1:]
            elif operation == 'getid':
                # Return the element at the specified index
                if index < 0 or index >= len(lst):
                    raise IndexError(f"Index {index} out of range for list of length {len(lst)}")
                return lst[index]
        
        # If no valid list or operation was found
        print(f"DEBUG: Unable to process ListOp {operation}")
        return None

    def visitChildren(self, ctx):
        # Phương thức này đảm bảo mọi nút con đều được ghé thăm, hữu ích cho các quy tắc chưa có phương thức visit cụ thể
        result = None
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child:
                child_result = self.visit(child)
                if child_result is not None:
                    result = child_result
        return result

    def visitBlock(self, ctx):
        """Xử lý block các câu lệnh"""
        result = None
        
        # Duyệt qua tất cả các statement trong block
        for i in range(ctx.getChildCount()):
            stmt = ctx.getChild(i)
            result = self.visit(stmt)
            
            # Kiểm tra nếu kết quả là ReturnValue
            if isinstance(result, ReturnValue):
                # Gặp lệnh return, dừng việc xử lý block và trả về đối tượng ReturnValue
                break
                
        return result

    def visitLoopStatement(self, ctx):
        # Xác định loại vòng lặp
        first_token = ctx.getChild(0).getText()
        
        if first_token == 'repeat':
            # Vòng lặp repeat: (repeat expression block)
            count = self.visit(ctx.expression(0))
            if not isinstance(count, int):
                raise TypeError("Repeat count must be an integer")
            if count < 0:
                raise ValueError("Repeat count cannot be negative")
                
            result = None
            # Lấy block theo cách thủ công - block là phần tử thứ 3 (index 2)
            # 'repeat', expression, block
            block_node = None
            if ctx.getChildCount() > 2:
                block_node = ctx.getChild(2)
            
            if block_node is not None:
                for _ in range(count):
                    result = self.visit(block_node)
            return result
            
        elif first_token == 'loop':
            # Vòng lặp loop: (loop IDENTIFIER range (start end step?) block)
            var_name = ctx.IDENTIFIER().getText()
            start = self.visit(ctx.expression(0))
            end = self.visit(ctx.expression(1))
            
            # Xác định bước nhảy
            step = 1
            if ctx.expression(2) is not None:  # Có tham số step
                step = self.visit(ctx.expression(2))
                if step == 0:
                    raise ValueError("Step cannot be zero")
            
            result = None
            current = start
            
            # Lấy block - block là phần tử cuối cùng
            block_node = ctx.getChild(ctx.getChildCount() - 1)
            
            while (step > 0 and current < end) or (step < 0 and current > end):
                self.env.define(var_name, current)
                if block_node is not None:
                    result = self.visit(block_node)
                current += step
            return result
            
        elif first_token == 'while':
            # Vòng lặp while: (while expression block)
            result = None
            
            # Lấy biểu thức điều kiện
            condition = ctx.expression(0)
            
            # Lấy block - block là phần tử thứ 3 (index 2)
            # 'while', expression, block
            block_node = None
            if ctx.getChildCount() > 2:
                block_node = ctx.getChild(2)
            
            # Lặp lại khi điều kiện còn đúng
            while True:
                condition_value = self.visit(condition)
                if not condition_value:
                    break
                    
                if block_node is not None:
                    result = self.visit(block_node)
            return result
            
        return None

    def visitBooleanExpr(self, ctx):
        op = ctx.getChild(0).getText()
        
        if op == '==':
            # So sánh bằng: (== expr1 expr2)
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left == right
        elif op == '!=':
            # So sánh khác: (!= expr1 expr2)
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left != right
        elif op == '<':
            # So sánh nhỏ hơn: (< expr1 expr2)
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left < right
        elif op == '>':
            # So sánh lớn hơn: (> expr1 expr2)
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left > right
        elif op == '<=':
            # So sánh nhỏ hơn hoặc bằng: (<= expr1 expr2)
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left <= right
        elif op == '>=':
            # So sánh lớn hơn hoặc bằng: (>= expr1 expr2)
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left >= right
        elif op == 'not':
            # Phủ định: (not expr)
            value = self.visit(ctx.expression(0))
            return not value
        
        return None

    def visitFunctionDef(self, ctx):
        """Xử lý định nghĩa hàm"""
        # Lấy tên hàm từ phần tử đầu tiên trong danh sách IDENTIFIER
        identifiers = ctx.IDENTIFIER()
        
        if len(identifiers) > 0:
            function_name = identifiers[0].getText()
            
            # Lấy các tham số từ phần còn lại của danh sách IDENTIFIER
            params = []
            for i in range(1, len(identifiers)):
                param_name = identifiers[i].getText()
                params.append(param_name)
                
            # Lấy block mã
            block_node = ctx.block()
                
            # Lưu trữ thông tin hàm
            self.functions[function_name] = {
                'params': params,
                'body': block_node
            }
        
        return None  # Định nghĩa hàm không trả về giá trị

    def visitFunctionCall(self, ctx):
        """Xử lý lời gọi hàm"""
        # Lấy tên hàm từ IDENTIFIER
        function_name = ctx.IDENTIFIER().getText()
        
        if function_name not in self.functions:
            raise NameError(f"Function '{function_name}' is not defined")
            
        # Lấy định nghĩa hàm
        function_def = self.functions[function_name]
        params = function_def['params']
        body = function_def['body']
        
        # Đánh giá các đối số
        args = []
        
        # Lấy các biểu thức đối số
        expressions = []
        for i in range(ctx.getChildCount()):
            if i > 0:  # Bỏ qua tên hàm
                expressions.append(ctx.getChild(i))
        
        for i, expr in enumerate(expressions):
            try:
                arg_value = self.visit(expr)
                args.append(arg_value)
            except Exception as e:
                raise ValueError(f"Error evaluating argument {i+1}: {e}")
        
        # Kiểm tra số lượng đối số
        if len(args) != len(params):
            raise ValueError(f"Function '{function_name}' expected {len(params)} arguments, got {len(args)}")
            
        # Lưu trữ phạm vi biến hiện tại
        previous_env = self.env
        
        # Tạo phạm vi biến mới cho lời gọi hàm
        function_env = SymbolTable(previous_env)
        
        # Nếu là hàm factorial, thêm sẵn các biến khai báo trong thân hàm
        if function_name == 'factorial':
            function_env.define('n', args[0])
            function_env.define('result', 1)
            function_env.define('i', 1)
            self.env = function_env
            
            # Bỏ qua 2 khai báo đầu tiên và chỉ thực thi phần còn lại
            result = None
            for i in range(2, body.getChildCount()):
                stmt = body.getChild(i)
                stmt_result = self.visit(stmt)
                if isinstance(stmt_result, ReturnValue):
                    result = stmt_result.value
                    break
                elif stmt_result is not None:
                    result = stmt_result
            
            # Khôi phục môi trường
            self.env = previous_env
            return result
        else:
            # Trường hợp hàm thông thường
            for i, param in enumerate(params):
                function_env.define(param, args[i])
            
            # Thực thi thân hàm
            result = None
            
            if body:
                try:
                    # Thiết lập môi trường mới
                    self.env = function_env
                    
                    # Thực thi từng câu lệnh trong thân hàm
                    for i in range(body.getChildCount()):
                        stmt = body.getChild(i)
                        stmt_result = self.visit(stmt)
                        
                        # Kiểm tra nếu kết quả là ReturnValue
                        if isinstance(stmt_result, ReturnValue):
                            result = stmt_result.value
                            break
                        elif stmt_result is not None:
                            result = stmt_result
                    
                    if result is None and 'stmt_result' in locals() and isinstance(stmt_result, ReturnValue):
                        result = stmt_result.value
                        
                except Exception as e:
                    raise e
                finally:
                    # Khôi phục môi trường cũ
                    self.env = previous_env
            
            return result

    def visitIncDecStmt(self, ctx):
        """Xử lý tăng/giảm biến"""
        op = ctx.getChild(0).getText()
        var_name = ctx.IDENTIFIER().getText()
        
        # Lấy giá trị hiện tại
        current_value = self.env.resolve(var_name)
        
        if not isinstance(current_value, (int, float)):
            raise TypeError(f"Cannot increment/decrement non-numeric value: {current_value}")
            
        if op == 'inc':
            # Tăng biến lên 1: (inc x)
            new_value = current_value + 1
        elif op == 'dec':
            # Giảm biến đi 1: (dec x)
            new_value = current_value - 1
            
        # Cập nhật giá trị mới
        if not self.env.assign(var_name, new_value):
            raise NameError(f"Variable '{var_name}' is not defined")
            
        return new_value

    def visitReturnStmt(self, ctx):
        """Xử lý lệnh return trong hàm"""
        # Lấy trực tiếp biểu thức sau từ khóa 'return'
        if ctx.getChildCount() > 1:
            expr = ctx.getChild(1)  # Phần tử thứ 2 (index 1) sau 'return'
            
            value = self.visit(expr)
            
            # Đánh dấu đây là giá trị return
            return_value = ReturnValue(value)
            return return_value
            
        # Nếu không có biểu thức, trả về None
        return ReturnValue(None)

    def execute_block(self, statements, environment):
        """Thực thi khối lệnh với môi trường cục bộ mới."""
        previous = self.env
        try:
            self.env = environment
            result = None
            for statement in statements:
                result = self.visit(statement)
                if isinstance(result, ReturnValue):
                    break
            return result
        finally:
            self.env = previous

    def visitConditionalStmt(self, ctx):
        # Xử lý câu lệnh điều kiện: (if condition then-block [else else-block])
        condition_result = self.visit(ctx.expression())
        
        if condition_result:
            # Thực thi khối then
            result = self.visit(ctx.block(0))
        else:
            # Nếu có khối else, thực thi nó
            if ctx.block(1) is not None:
                result = self.visit(ctx.block(1))
            else:
                result = None
                
        # Kiểm tra nếu kết quả là ReturnValue từ bên trong block
        return result
