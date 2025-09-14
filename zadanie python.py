print("hello")

print(int(input()) + int(input()))

# print(int(input())+int(input()))
a = int(input())
b = int(input())
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

a=int(input())
if a%2==0: print("четное")
else:  print("нечетное")

a=int(input())
if a<0:
    print("-")
elif a==0:
    print("=0")
elif a>0:
    print("+")

a=int(input())
for b in range(11):
    print(b*a)

def factorial(x):
    ans=1

    if x <0:
        raise ValueError('x must be greater than 0')

    for i in range(1, x+1):
        ans *=1

    return ans

print(factorial(7))

def is_prime(n):

    if n<= 1:
        return False
    for i in range(2, int(n**0,5+1)):
        if n % i == 0:
            return False
    return True
print(is_prime(11))
