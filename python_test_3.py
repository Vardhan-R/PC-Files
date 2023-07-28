# from built_modules import import_number_system_converter as nsc
# print(type(nsc.convertNum("1001", 2, 10)))
import numpy as np

class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

"""Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

def abc(x: int, y: int) -> int:
    '''
    returned
    >>> factorial(1e100)
    >>> colour.BOLD + pqq + colour.END
    >>> if a == b:
    print(i)
    '''
    return x + y

print(abc(4, 5))

print(colour.RED + 'pqq' + colour.END)

print(np.argwhere(np.array([9, 5, 6]) == 9))

# from built_modules.test_folder import import_number_system_converter as nsc
# print(type(nsc.convertNum("1001", 2, 10)))