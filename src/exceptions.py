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


class OnionIndexError(OnionRuntimeError):
    """Raised when a list index is out of bounds"""


class OnionRecursionError(OnionRuntimeError):
    """Raised when recursion depth exceeds the maximum allowed"""


class OnionTimeoutError(OnionRuntimeError):
    """Raised when execution time exceeds the maximum allowed"""


class OnionDivisionByZeroError(OnionRuntimeError):
    """Raised when dividing by zero"""


class OnionEmptyListError(OnionRuntimeError):
    """Raised when attempting to perform an operation on an empty list that requires elements"""


class OnionLoopRangeError(OnionRuntimeError):
    """Raised when a loop range is invalid (e.g., negative step with increasing range)"""


class OnionAssignmentError(OnionRuntimeError):
    """Raised when an assignment operation fails due to scope or other issues"""


class OnionOperationError(OnionRuntimeError):
    """Raised when an operation is performed on incompatible types or values"""


class OnionInterpolationError(OnionRuntimeError):
    """Raised when string interpolation fails"""
