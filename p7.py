# prime numbers from 1 to 20: 2,3,5,7,11,13,17,19

from itertools import count, takewhile

def primes(n):
    "Generate prime numbers up to n"
    seen = list()
    for i in xrange(2, n + 1):
        if all(map(lambda prime: i % prime, seen)):
            seen.append(i)
            yield i

def smallest(n):
    result = 1
    for prime in primes(n):
        bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1))))
        # we could just take last instead of max()
        result *= bprime
    return result

print smallest(20)