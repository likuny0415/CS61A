""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def prime_helper(a, n):
        if n == 2:
            return True;
        elif n == a:
            return True;
        elif n % a == 0:
            return False
        else:
            return prime_helper(a+1, n)
    return prime_helper(2, n)



def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE "
    def gcd_helper(i, largest, a, b):
        if i > min(a,b):
            return largest
        elif a % i == 0 and b % i == 0:
            largest = i
            return gcd_helper(i+1, largest, a, b)
        else:
            return gcd_helper(i+1, largest, a, b)
    return gcd_helper(1, 1, a, b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def ten_helper(n, target):
        if n == 0:
            return 0
        elif n % 10 + target == 10:
            return 1 + ten_helper(n // 10, target)
        else:
            return ten_helper(n // 10, target)
    if n < 10:
        return 0
    else:
        return ten_helper(n // 10, n % 10) + ten_pairs(n // 10)
