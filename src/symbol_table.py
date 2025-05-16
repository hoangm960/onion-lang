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

    # Lookup a symbol in the current scope only
    def lookup_current_scope(self, name):
        current_scope = self.current_scope()
        if name in current_scope:
            return current_scope[name]
        return None

    # Lookup a symbol from the top scope down to the global
    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    # Create a deep copy of the symbol table
    def clone(self):
        """Create a deep copy of the symbol table, safely handling unpicklable items in scopes."""
        import copy

        new_table = SymbolTable()  # Initializes with its own empty scopes [{}]
        cloned_scopes_list = []

        for original_scope_dict in self.scopes:
            new_scope_dict = {}
            for key, value in original_scope_dict.items():
                try:
                    # Attempt to deepcopy the value.
                    # copy.deepcopy uses __getstate__/__setstate__ for custom objects like Lambda/SymbolTable
                    # if they don't have __deepcopy__.
                    new_scope_dict[key] = copy.deepcopy(value)
                except TypeError as e:
                    # Check if the TypeError is related to pickling (which deepcopy might use)
                    # Common messages include "cannot pickle" or involve specific unpicklable types.
                    error_str = str(e).lower()
                    if "pickle" in error_str or "textiowrapper" in error_str or "io.textiowrapper" in error_str:
                        # Skip this value as it's unpicklable/problematic for deepcopy
                        pass
                    else:
                        # Re-raise other TypeErrors not related to pickling
                        raise
                except Exception:
                    # Catch any other unexpected error during deepcopy (e.g., recursion limits on complex objects)
                    # For lambda environment capture, it's safer to skip the problematic item.
                    # Optionally, log a warning here.
                    pass  # Skip the value
            cloned_scopes_list.append(new_scope_dict)
        
        new_table.scopes = cloned_scopes_list
        if new_table.scopes:
            new_table.global_scope = new_table.scopes[0]
        else:
            # This case implies self.scopes was empty or all its contents were unpicklable.
            # Ensure new_table is still valid.
            new_table.global_scope = {}
            new_table.scopes = [new_table.global_scope]
            
        return new_table
