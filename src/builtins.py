from src.exceptions import (
    OnionArgumentError,
    OnionNameError,
    OnionRuntimeError,
    OnionTypeError,
)


class BuiltInFunctions:
    """Registry for built-in functions"""

    registry = {}

    @classmethod
    def register_defaults(cls):
        cls.register("len", cls._len)
        cls.register("typeof", cls._typeof)
        cls.register("copy", cls._copy)
        cls.register("fact", cls._fact)

    @classmethod
    def register(cls, name, func):
        cls.registry[name] = func

    @classmethod
    def execute(cls, name, interpreter, args):
        if name not in cls.registry:
            raise OnionNameError(f"Undefined built-in function '{name}'")
        return cls.registry[name](interpreter, args)

    @staticmethod
    def _len(interpreter, args):
        if len(args) != 1:
            raise OnionArgumentError(f"len() expects 1 argument, got {len(args)}")
        value = args[0]
        if isinstance(value, (list, str)):
            return len(value)
        raise OnionTypeError(
            f"len() requires a list or string, got {type(value).__name__}"
        )

    @staticmethod
    def _typeof(interpreter, args):
        if len(args) != 1:
            raise OnionArgumentError(f"typeof() expects 1 argument, got {len(args)}")
        value = args[0]
        if isinstance(value, bool):
            return "bool"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "string"
        if isinstance(value, list):
            return "list"
        return type(value).__name__

    @staticmethod
    def _copy(interpreter, args):
        """Built-in copy function for lists."""
        if len(args) != 1:
            raise OnionArgumentError(f"copy() expects 1 argument, got {len(args)}")
        value = args[0]
        if isinstance(value, list):
            return value[:]  # Return a shallow copy
        # Can optionally add support for copying other types if needed
        raise OnionTypeError(
            f"copy() currently only supports lists, got {type(value).__name__}"
        )

    @staticmethod
    def _fact(interpreter, args):
        if len(args) != 1:
            raise OnionArgumentError(f"fact() expects 1 argument, got {len(args)}")
        n = args[0]
        if not isinstance(n, int):
            raise OnionTypeError(f"fact() requires an integer, got {type(n).__name__}")
        if n < 0:
            raise OnionRuntimeError(
                "fact() cannot compute factorial of a negative number"
            )
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
