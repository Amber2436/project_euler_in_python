def _is_increasing(x_as_list):
    """
    Returns True if no digit is exceeded by the digit to its left
    """
    return sorted(x_as_list) == x_as_list

def _is_decreasing(x_as_list):
    """
    Returns True if no digit is exceeded by the digit to its right
    """
    return sorted(x_as_list, reverse=True) == x_as_list

def is_bouncy(x):
    """
    Returns True if x is bouncy i.e is neither increasing or decreasing.
    """
    x_as_list = list(str(x))
    return not (_is_increasing(x_as_list) or _is_decreasing(x_as_list))


def solution():
    """
    """
    x = 21780     # counter
    count = 21780*0.9 # number of bouncy numbers seen

    while count * 100 / x != 99:
        count += bool(is_bouncy(x))
        x += 1

    return x
		 
print solution()
