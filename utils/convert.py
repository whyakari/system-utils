from .types import gibibytes

def gb_to_bytes(gb: gibibytes) -> int:
    """function for converter gibibytes in bytes."""
    bytes_per_gibibyte = 1073741824
    bytes = gb * bytes_per_gibibyte
    return bytes
