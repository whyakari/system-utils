from .types import (
    gibibytes, 
    terabytes, 
    megabytes
)

def tb_to_bytes(tb: terabytes) -> int:
    """Converte terabytes em bytes."""
    bytes_per_terabyte = 1099511627776
    bytes = tb * bytes_per_terabyte
    return bytes


def gb_to_bytes(gb: gibibytes) -> int:
    """Converte gibibytes em bytes."""
    bytes_per_gibibyte = 1073741824
    bytes = gb * bytes_per_gibibyte
    return bytes

def mb_to_bytes(mb: megabytes) -> int:
    """Converte megabytes em bytes."""
    bytes_per_megabyte = 1048576
    bytes = mb * bytes_per_megabyte
    return bytes

