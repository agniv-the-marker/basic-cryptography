from collections import Counter as counter

def euler_phi(n: int) -> int:
    """Computes the euler phi (totient) function.
    
    Args:
        n

    Returns:
        phi(n) counting 
        |{0 <= a < n: gcd(a,n)=1}|

    Examples:
        >>> euler_phi(100)
        40
    """
    toitent = n
    for p in factor(n): toitent = (p-1) * toitent // p
    return toitent
    # return len([i for i in range(n) if gcd(i,n) == 1])

def is_prime(n: int) -> bool:
    """Determine if n is prime."""
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

def next_prime(n: int) -> int:
    """Return the first prime >= n."""
    if n == 2: return 3
    if n % 2 == 0: n -= 1
    while not is_prime(n):
        n += 2
    return n + 1

def factor(n: int):
    """What data types should factor return?
    What is the cleanest way to implement trial division?"""
    factors = counter()
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 2
    if n > 1:
        factors[n] += 1
    return factors

def print_factor(n, rep=None):
    factors = factor(n)
    if rep:
        f = f'{rep} = '
    else:
        f = f'{n} = '
    for fac in factors:
        f += f'{fac}'
        if factors[fac] > 1:
            f += f'^{factors[fac]}'
        f += ' * '
    return f[:-3]

"""
When k = 2, 4, 6, 8, we have 10^2k - 10^k + 1 is prime. 
However, according to https://oeis.org/A187868, the next one is HUGE.

We have:

2^1 + 1 = 3
2^2 + 1 = 5
2^3 + 1 = 3^2
2^4 + 1 = 17
2^5 + 1 = 3 * 11
2^6 + 1 = 5 * 13
2^7 + 1 = 3 * 43
2^8 + 1 = 257
2^9 + 1 = 3^3 * 19
2^10 + 1 = 5^2 * 41
2^11 + 1 = 3 * 683
2^12 + 1 = 17 * 241
2^13 + 1 = 3 * 2731
2^14 + 1 = 5 * 29 * 113
2^15 + 1 = 3^2 * 11 * 331
2^16 + 1 = 65537
2^17 + 1 = 3 * 43691
2^18 + 1 = 5 * 13 * 37 * 109
2^19 + 1 = 3 * 174763
2^20 + 1 = 17 * 61681
2^21 + 1 = 3^2 * 43 * 5419
2^22 + 1 = 5 * 397 * 2113
2^23 + 1 = 3 * 2796203
2^24 + 1 = 97 * 257 * 673
2^25 + 1 = 3 * 11 * 251 * 4051
2^26 + 1 = 5 * 53 * 157 * 1613
2^27 + 1 = 3^4 * 19 * 87211
2^28 + 1 = 17 * 15790321
2^29 + 1 = 3 * 59 * 3033169
2^30 + 1 = 5^2 * 13 * 41 * 61 * 1321
2^31 + 1 = 3 * 715827883
2^32 + 1 = 641 * 6700417
2^33 + 1 = 3^2 * 67 * 683 * 20857
2^34 + 1 = 5 * 137 * 953 * 26317
2^35 + 1 = 3 * 11 * 43 * 281 * 86171
2^36 + 1 = 17 * 241 * 433 * 38737
2^37 + 1 = 3 * 1777 * 25781083
2^38 + 1 = 5 * 229 * 457 * 525313
2^39 + 1 = 3^2 * 2731 * 22366891
2^40 + 1 = 257 * 4278255361
2^41 + 1 = 3 * 83 * 8831418697
2^42 + 1 = 5 * 13 * 29 * 113 * 1429 * 14449
2^43 + 1 = 3 * 2932031007403
2^44 + 1 = 17 * 353 * 2931542417
2^45 + 1 = 3^3 * 11 * 19 * 331 * 18837001
2^46 + 1 = 5 * 277 * 1013 * 1657 * 30269
2^47 + 1 = 3 * 283 * 165768537521
2^48 + 1 = 193 * 65537 * 22253377
2^49 + 1 = 3 * 43 * 4363953127297
2^50 + 1 = 5^3 * 41 * 101 * 8101 * 268501

Note for k = 1, 2, 4, 8, 16, we have 2^k + 1 is prime. 

k must be a power of two at each point.

Look at the minimal prime factor of each one:

3, 5, 3, 17, 3, 5, 3, 257, 3, 5, 3, 17, 3, 5, 3, 65537, 3, 5, 3, 17, 3, 5, 3, 97, 3, 5, 3, 17, 3, 5, 3, 641, 3, 5, 3, 17, 3, 5, 3, 257, 3, 5, 3, 17, 3, 5, 3, 193, 3, 5

This is periodic mod 8.

Some factorization:

2**58 + 1 = 5 * 107367629 * 536903681
10^22 + 1 = 89 * 101 * 1052788969 * 1056689261

"""

if __name__ == "__main__":
    print(print_factor(10**22 + 1, '10^22 + 1'))
