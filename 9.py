def is_prime(n):

    if n<= 1:
        return False
    for i in range(2, int((n ** 0.5) + 1)):
        if n % i == 0:
            return False
    return True
print(is_prime(11))

def factorial(x):
    ans=1

    if x <0:
        raise ValueError('x must be greater than 0')

    for i in range(1, x+1):
        ans *=i

    return ans

print(factorial(7))

lst=[ int(input()) for i in range(3)]

print(min(lst))
print(max(lst))