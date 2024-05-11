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

if __name__ == "__main__":

    ciphertext = [87, 250, 18, 249, 54, 215, 17, 249, 18, 44, 249, 169, 249, 44, 63, 113, 28, 250, 249, 224, 28, 28, 113, 249, 17, 44, 134, 124, 249, 159, 164, 38, 53, 5, 28, 249, 215, 28, 124, 28, 111, 180, 26, 44, 134, 124, 249, 28, 17, 28, 38, 249, 188, 164, 245, 28, 249, 53, 5, 53, 113, 28, 249, 188, 53, 250, 113, 28, 124, 250, 38, 58, 255, 33, 44, 250, 249, 53, 250, 18, 249, 44, 250, 180, 74, 28, 188, 44, 54, 249, 113, 215, 28, 249, 113, 44, 44, 113, 215, 218, 53, 38, 113, 28, 249, 53, 250, 18, 249, 113, 215, 28, 249, 18, 53, 250, 18, 124, 134, 63, 63, 249, 53, 18, 38, 102, 180, 58, 255, 33, 87, 250, 18, 249, 18, 164, 18, 249, 113, 215, 28, 164, 124, 249, 124, 164, 18, 164, 250, 5, 249, 28, 17, 28, 38, 249, 124, 164, 5, 215, 113, 249, 113, 215, 124, 44, 134, 5, 215, 249, 17, 44, 134, 124, 249, 38, 164, 18, 28, 111, 180, 87, 250, 18, 249, 18, 164, 18, 249, 113, 215, 28, 164, 124, 249, 28, 17, 28, 38, 249, 188, 164, 245, 28, 249, 134, 250, 54, 53, 38, 215, 28, 18, 249, 218, 188, 53, 113, 113, 28, 124, 38, 249, 124, 164, 18, 28, 102, 180, 87, 250, 18, 249, 223, 28, 53, 113, 215, 111, 249, 53, 188, 44, 63, 113, 111, 58, 255, 33, 5, 164, 5, 53, 250, 113, 164, 135, 53, 188, 188, 17, 249, 18, 44, 54, 250, 180, 151, 124, 44, 139, 164, 250, 5, 249, 113, 215, 124, 44, 134, 5, 215, 249, 17, 44, 134, 58, 255, 33, 113, 44, 54, 53, 124, 18, 249, 224, 28, 111, 249, 244, 249, 28, 159, 28, 124, 224, 44, 124, 28, 148, 180, 87, 250, 18, 249, 54, 215, 28, 250, 249, 113, 215, 28, 17, 249, 18, 124, 53, 5, 5, 28, 18, 249, 17, 44, 134, 124, 249, 124, 28, 113, 135, 215, 164, 250, 5, 249, 63, 188, 28, 38, 215, 111, 180, 26, 44, 134, 124, 249, 113, 124, 28, 224, 139, 188, 164, 250, 5, 249, 215, 53, 250, 18, 38, 249, 113, 215, 53, 113, 249, 250, 164, 5, 215, 113, 249, 113, 215, 124, 44, 134, 5, 215, 249, 74, 53, 188, 113, 164, 224, 44, 124, 28, 58, 255, 33, 180, 205, 215, 53, 113, 249, 188, 53, 38, 113, 249, 250, 164, 5, 215, 113, 249, 44, 250, 249, 113, 215, 28, 249, 139, 53, 188, 188, 44, 113, 249, 124, 44, 134, 250, 18, 38, 111, 249, 18, 164, 18, 249, 17, 44, 134, 111, 180, 96, 215, 53, 245, 164, 250, 5, 111, 249, 18, 164, 18, 249, 17, 44, 134, 249, 18, 28, 250, 17, 249, 113, 215, 28, 249, 113, 164, 135, 245, 28, 113, 111, 249, 151, 44, 28, 102]

    block_size = 1

    mod = next_prime(256**block_size)

    for key in range(1, mod - 1, 2):
        try:
            print(block_decode(exp_encrypt(ciphertext, key, mod), block_size))
            print(f'key = {multiplicative_inverse(key, mod-1)}\n')
            # break
        except:
            pass

