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
