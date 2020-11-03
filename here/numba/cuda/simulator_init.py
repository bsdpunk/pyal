from .simulator import *


def is_available():
    """Returns a boolean to indicate the availability of a CUDA GPU.
    """
    # Simulator is always available
    return True


def cuda_error():
    """Returns None or an exception if the CUDA driver fails to initialize.
    """
    # Simulator never fails to initialize
    return None



