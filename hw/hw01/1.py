def is_prime(n):
    if (n < 3):
        return n > 1;
    num = n - 1;
    while num > 1:
        res = n % num;
        if (res == 0):
            return False;
        num -= 1;
    return True;

print(is_prime(33))
