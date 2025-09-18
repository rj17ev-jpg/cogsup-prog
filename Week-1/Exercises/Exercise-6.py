"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

list_of_primes = []
def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    if n % d == 0:
        return True

def is_prime(n):
    if n >=2:
        if not any(is_factor(i,n) for i in range((n)**0.5)):
            if n not in list_of_primes:
                list_of_primes.append(n)
                return True
    

for n in range(2,1000):
    is_prime(n)


print(list_of_primes)