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

def multiplicative_inverse(a, n):
    """Find a^(-1) mod n"""
    for i in range(n):
        if (a * i) % n == 1:
            return i
    raise ValueError(f"{a} has no inverse mod {n}")

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

if __name__ == "__main__":
    key = [1, 2]
    n = 2**32
    msg = [1685022522, 552640400, 3053453312]

    assert msg == affine_decrypt(affine_encrypt(msg, key, n), key, n)