# prime numbers.


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

l = [1,2,-3,4,5,6,7,8,9,10,11,12,13,14,15]

result = list(filter(is_prime, l))
print(result)