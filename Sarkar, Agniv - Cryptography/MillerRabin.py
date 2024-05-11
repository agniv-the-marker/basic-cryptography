import random

def sharkovskii_representation(n: int) -> (int, int):
    """Returns the Sharkovskii Representation of n."""
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return (e, n)

def is_strong_pseudoprime(n: int, b: int) -> bool:
    """Perform Miller-Rabin test on base b."""
    if n % 2 == 0 and n > 2: return False
    _, exp = sharkovskii_representation(n - 1)
    root = pow(b, exp, n)
    return root in {1, n - 1}

def is_probably_prime(n: int, guesses: int = 1000) -> bool:
    """Perform Miller-Rabin test for random bases."""
    for _ in range(max(n, guesses)):
        b = random.randint(2, n-2)
        if not is_strong_pseudoprime(n, b):
            return False
    return True
    
def next_probable_prime(n: int) -> int:
    """Return the first int >= n which passes is_probably_prime."""
    if n <= 2: return 2
    if n == 3: return 3
    if n % 2 == 0: n += 1
    while not is_probably_prime(n):
        n += 2
    return n

if __name__ == "__main__":

    ns = [
    168003672409, # not prime
    16800367240931, # probably prime?
    271017128857254504705902822401, # not prime
    27101712885725450470590282240137, # probably prime
    496757958275272577729908884399939997312496935424849671193310676199353, # probably prime
    49675795827527257772990888439993999731249693542484967119331067619934769 # not prime
    ]

    # print(list(map(is_probably_prime, ns)))

    false_roots = [
    (168003672409, 42000918102),
    (271017128857254504705902822401, 529330329799325204503716450),
    (49675795827527257772990888439993999731249693542484967119331067619934769, 24837897913763628886495444219996999865624846771242483559665533809967384)
    ]

    ns = [10 ** (100 * i - 1) for i in range(1,9)]
    # for i, num in [(100*i, 10**(100*i - 1)) for i in range(1, 9)]:
    #     print(i, next_probable_prime(num) - 10**(i - 1))
    #     print()

    n = 7
    while True:
        if not is_prime(n):
            if is_strong_pseudoprime(n, 2):
                print(n)
                break
        n += 2