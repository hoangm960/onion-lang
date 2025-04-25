from src.exceptions import OnionArgumentError, OnionNameError, OnionTypeError


class BuiltInFunctions:
    """Registry for built-in functions"""

    registry = {}

    @classmethod
    def register_defaults(cls):
        """Register core built-in functions"""
        cls.register("len", cls.len)
        cls.register("typeof", cls.typeof)

    @classmethod
    def register(cls, name, func):
        """Register a new built-in function"""
        cls.registry[name] = func

    @staticmethod
    def execute(name, interpreter, args):
        """Execute a built-in function"""
        if name not in cls.registry:
            raise OnionNameError(f"Undefined built-in function: {name}")
        return cls.registry[name](interpreter, args)

    @staticmethod
    def len(interpreter, args):
        if len(args) != 1:
            raise OnionArgumentError("len() expects exactly 1 argument")
        value = args[0]
        if isinstance(value, (list, str)):
            return len(value)
        raise OnionTypeError("len() requires string or list")

    @staticmethod
    def typeof(interpreter, args):
        if len(args) != 1:
            raise OnionArgumentError("typeof() expects exactly 1 argument")
        value = args[0]
        return type(value).__name__
