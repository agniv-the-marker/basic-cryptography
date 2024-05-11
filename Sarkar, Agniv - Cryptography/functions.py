"""Functions we will continue to use in future assignments."""

from collections import Counter as counter

def block_encode(message: str, block_size: int = 1) -> list[int]:
    """Perform our encoding scheme to convert a string into a list of integers.
    The string is encoded into UTF-8 and then split into consecutive blocks.
    Each block of bytes is then returned as the corresponding order, in big-byte
    order.

    Args:
        message: string to be encoded
        block_size: how many bytes each block contains. The final block is padded
            with zeros.

    Returns:
        blocks: a list of integers that encode the message

    Examples:
        >>> block_encode('dog: 🐶', 4)
        [1685022522, 552640400, 3053453312]
    """
    seq = message.encode()
    seq += int(0).to_bytes((-1 * len(seq)) % block_size, 'big')
    blocks = [seq[i:i+block_size] for i in range(0, len(seq), block_size)]
    return [int.from_bytes(block, 'big') for block in blocks]

def block_decode(blocks: list[int], block_size: int = 1) -> str:
    """Performs the inverse of block_encode

    Args:
        blocks: a list of integers that encode the message
        block_size: how many bytes each block contains. The final block is padded
            with zeros.

    Returns:
        message: the original string

    Examples:
        >>> block_decode([1685022522, 552640400, 3053453312], 4)
        'dog: 🐶'
    """
    decoded = [block.to_bytes(block_size, 'big') for block in blocks]
    decoded[-1] = decoded[-1].rstrip(int(0).to_bytes(1, 'big'))
    seq = b''
    for d in decoded:
        seq += d
    return seq.decode()

def affine_encrypt(plaintext: list[int], key: tuple[int, int], block_size: int = 1) -> list[int]:
    """Performs affine encryption on blocks of encoded integers,
    using the function f(x) = ax + b mod (n = 256^block_size).

    Args:
        plaintext: a list of integers that encode the message
        key: (a, b) to perform f(x) = ax + b mod n 
        block_size: how many bytes each block contains

    Returns:
        ciphertext: encrypted integers

    Examples:
        >>> affine_encrypt([1685022522, 552640400, 3053453312], (123456789, 987654321), 4)
        [4115223155, 1183960961, 685664433]
    """
    return [(b*key[0] + key[1]) % (256 ** block_size) for b in plaintext]

def gcd(a: int, b: int) -> int:
    """Run the euclidean algorithm to compute g = gcd(a,b).

    Args:
        a, b: ints

    Returns:
        g = gcd(a,b)

    Examples:
        >>> gcd(2024, 748)
        44
    """
    if b == 0: return a
    return gcd(b, a%b)

def egcd(a: int, b: int) -> tuple[int, int, int]:
    """Run the extended euclidean algorithm to compute g = gcd(a,b) and return x,y such that ax+by = g.

    Args:
        a, b: ints

    Returns:
        Triple g, x, y, where g = gcd(a,b) and ax+by = g.

    Examples:
        >>> egcd(2024, 748)
        (44, -7, 19)
    """
    x, y, next_x, next_y = 0, 1, 1, 0
    while a:
        b, a, x, y, next_x, next_y = a, b % a, next_x, next_y, x - next_x * (b // a), y - next_y * (b // a)
    return b, x, y

def multiplicative_inverse(a: int, n: int) -> int:
    """Find the multiplicative inverse a^{-1} mod n.
  
    Args:
      a, n: ints

    Returns:
      Multiplicate inverse, an integer x such that ax=1 mod n

    Examples:
        >>> multiplicative_inverse(33, 256)
        225

    Raises:
      ValueError if gcd(a,n) != 1, because the inverse does not exist
    """
    if gcd(a, n) != 1: raise ValueError
    return (egcd(n, a)[2] + n) % n

def affine_decrypt(ciphertext: list[int], key: tuple[int, int], block_size: int = 1) -> list[int]:
    """Performs the inverse of affine_encrypt.

    Args:
        ciphertext: encrypted integers
        key: (a, b) to invert f(x) = ax + b mod n 
        block_size: how many bytes each block contains

    Returns:
        plaintext: a list of integers that encode the message

    Examples:
        >>> affine_decrypt([4115223155, 1183960961, 685664433], (123456789, 987654321), 4)
        [1685022522, 552640400, 3053453312]
    """
    inv = multiplicative_inverse(key[0], 256**block_size)
    return [inv * (b - key[1]) % 256**block_size for b in ciphertext]

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
    if is_prime(n): return n
    if n % 2 == 0: n += 1
    while not is_prime(n):
        n += 2
    return n

def factor(n: int):
    """What data types should factor return?
    What is the cleanest way to implement trial division?"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)
    return counter(factors)

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

def exp_encrypt(plaintext: list[int], key: int, p: int) -> list[int]:
    """Performs the exponentiation cipher on blocks of encoded integers,
    using the function f(x) = x^k mod p.

    Args:
        plaintext: a list of integers that encode the message
        key: k to perform f(x) = x^k mod p
        p: size of the modulus, needs to be a prime bigger than 256^block_size

    Returns:
        ciphertext: encrypted integers

    Examples:
        >>> exp_encrypt([61599, 39041], 12345, 256**2+1)
        [59696, 1847]

    Raises:
        ValueError if f(x) is not invertible
    """
    assert gcd(key, p-1) == 1, ValueError
    return [pow(x, key, p) for x in plaintext]

def exp_decrypt(ciphertext: list[int], key: int, p: int) -> list[int]:
    """Performs the inverse of exp_encrypt.

    Args:
        ciphertext: encrypted integers
        key: k to invert f(x) = x^k mod p
        p: size of the modulus, needs to be a prime bigger than 256^block_size

    Returns:
        plaintext: a list of integers that encode the message

    Examples:
        >>> exp_decrypt([59696, 1847], 12345, 256**2+1)
        [61599, 39041]
    Raises:
        ValueError if f(x) is not invertible
    """
    assert gcd(key, p-1) == 1, ValueError
    return exp_encrypt(ciphertext, multiplicative_inverse(key, p-1), p)

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
    power, exp = sharkovskii_representation(n - 1)
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