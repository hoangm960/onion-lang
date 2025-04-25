class OnionRuntimeError(Exception):
    """Base class for all Onion runtime exceptions"""


class OnionTypeError(OnionRuntimeError):
    """Raised for type-related errors"""


class OnionNameError(OnionRuntimeError):
    """Raised for undefined variable/function errors"""


class OnionArgumentError(OnionRuntimeError):
    """Raised for incorrect function arguments"""


class OnionPrintError(OnionRuntimeError):
    """Raised for wrong print type/format"""
