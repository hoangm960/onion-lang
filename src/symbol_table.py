class SymbolTable:
    """Bảng ký hiệu phân cấp để quản lý phạm vi biến."""

    def __init__(self, parent=None):
        self.global_scope = {}  # lưu trữ biến ở phạm vi hiện tại
        self.scopes = [self.global_scope]  # bảng ký hiệu phạm vi cha

    # Get the current scope from top of stack
    def current_scope(self):
        return self.scopes[-1]

    # Enter a new scope by pushing an empty dictionary onto the stack
    def push_scope(self):
        self.scopes.append({})

    # Exit the current scope
    def pop_scope(self):
        self.scopes.pop()

    # Define a new symbol in the current scope
    def define(self, name, value):
        self.current_scope()[name] = value

    # Lookup a symbol from the top scope down to the global
    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None
