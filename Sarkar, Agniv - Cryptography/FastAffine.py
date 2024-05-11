from time import time
from BlockEncoder import *
from EuclidanAlg import *

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
    return (egcd(n, a)[2] + n) % n

def slow_multiplicative_inverse(a, n):
    """Find a^(-1) mod n"""
    for i in range(n):
        if (a * i) % n == 1:
            return i
    raise ValueError(f"{a} has no inverse mod {n}")

def affine_decrypt(ciphertext: list[int], key: tuple[int, int], block_size: int = 1, slow: bool = False) -> list[int]:
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
    if slow:
        inv = slow_multiplicative_inverse(key[0], 256**block_size)
    else:
        inv = multiplicative_inverse(key[0], 256**block_size)
    return [inv * (b - key[1]) % 256**block_size for b in ciphertext]

if __name__ == "__main__":
    # Problem 1
    k = (12345, 6789)
    b = 2
    ciphertext = [18578, 40613, 55100, 5209, 18690, 46055, 61329, 36185, 46539, 61329,
    4773, 15818, 2961, 11685, 17553, 30608, 62629, 31974, 19202, 28661, 519, 1873, 486,
    62885, 19629, 56210, 64713, 58400, 46566, 32401, 45143, 40613, 62268, 24352, 61783,
    11522, 5209, 55461, 32236, 24270, 32236, 36615, 4297, 15760, 18294, 58457, 28661,
        25209, 56485, 34221, 9504, 58400, 26599, 13315, 4261, 32236, 12837, 42244, 21849,
        18853, 47781, 3473, 15364, 28661, 41365, 13221, 27026, 89, 38005, 60902, 27422,
        46566, 26370, 486, 53963, 4327, 48130, 28987, 57347, 65369, 25660, 17091]

    start = time()
    msg = block_decode(affine_decrypt(ciphertext, k, b, True), b)
    end = time()
    print(f'Problem 1: {msg}')
    print(f'slow : {end - start}')
    start = time()
    msg = block_decode(affine_decrypt(ciphertext, k, b, False), b)
    end = time()
    print(f'fast : {end - start}\n')

    # Problem 2
    ## This one should now only be possible using the more efficient decryption
    k = (1234567891011121314151617,12345678910111213141516)
    b = 10
    ciphertext = [259354354081382997634861, 1153404156395300420669466, 
    1182815096041759766922492, 1016697241573828548594556, 1100408969930801932806444, 
    35336582296338114704941, 847146856907634406543035, 944392590972975682980980, 
    812202576383251713044269, 369681420691784722681197, 137995999535082023891840, 
    334213349236498322374331, 845043018822387733530618, 271754333468590267416076]

    msg = block_decode(affine_decrypt(ciphertext, k, b, False), b)
    print(f'Problem 2: {msg}\n')

    ## Now we are going to see why affine encryption is not actually used in practice

    ## Next two examples should start with 'Eric'

    # Problem 3
    k = (54321, 1234)
    b = 2
    ciphertext = [47012, 11461, 30421, 60945, 61054, 44786, 5137, 48882, 11782, 5028, 
    48882, 39207, 22997, 62857, 43989, 51097, 17414, 29426, 62699, 36338, 31075, 39207, 
    11499, 4338, 42023, 51097, 49888, 35541, 11499, 48882, 27834, 45743, 19206, 51698, 
    32295, 30421, 26821, 59300, 56958, 46066, 34528, 30116, 834, 61479, 18848]

    msg = block_decode(affine_decrypt(ciphertext, k, b, False), b)
    print(f'Problem 3: {msg}\n')

    # Problem 4
    ciphertext = [1807530757, 3497324623, 3875106907, 3213779065, 2351625792, 183994054, 
    1539632776, 214280319, 1734049720, 3319252616, 608637299, 3964779399, 2244955897, 
    3102260548, 2498212624, 3781381786, 2820547451, 2425917173, 2226335112, 1128184581, 
    1385810744, 2769981173, 2724238069, 153991043, 2121234718, 1145508211, 3553949248, 
    183994054, 1539632776, 1943287151, 3373667321, 4177908788, 3102260548, 2723100040, 
    164487614, 1198305416, 3257165960, 2942525626, 2690390781, 2687817012, 2108383418, 
    3820711043, 3038246531, 1157741620, 3428905603, 476815936, 401811848, 780981946, 
    3753257347, 2871317812, 2821843848, 869693576, 2060406521, 2432806141, 3908215360, 
    4149778421, 2345557178, 2434857351, 3118660676, 2002308148, 1789770632, 3366611080, 
    4127343790, 1409288437, 2599406644, 2432806141, 4113333186, 3686902659, 3936943495, 
    66005384, 3279937785, 1680135476, 3188321084, 816270900, 4188036282, 1157741620, 
    220439289, 670212672, 643056180, 132967169, 2771413128, 3148333234, 1915327221, 2263954600]

    b = 4

    for end in range(256):
        last = 256**(b-1) * end
        k = [0, 0]
        k[0] = (ciphertext[-1] - ciphertext[0]) * multiplicative_inverse(last - block_encode('Eric', 4)[0], 256**b)
        k[0] %= 256**b
        k[1] = ciphertext[-1] - last * k[0]
        k[1] %= 256**b
        try:
            msg = block_decode(affine_decrypt(ciphertext, k, b), b)
        except:
            continue
        print(f'Problem 4: {msg}')
        print(f'Block : {b}')
        print(f'Key : {k}\n')

    # Problem 5
    ciphertext = [27193, 11409, 29220, 42817, 42686, 21599, 6855, 11409, 26311, 3195, 
    43681, 27174, 43207, 42534, 8849, 29220, 13177, 34095, 30445, 23666, 37054, 57325, 
    11409, 43444, 42686, 15393, 62984, 35217, 62663, 2076, 33169, 54765, 54054, 64341, 
    9737, 3985, 62037, 27326, 27904, 16785, 29220, 43954]

    b = 2
    for a in range(1, 256**b, 2):
        k = [a, (ciphertext[0] - 21608 * a) % 256**b]
        if (21608 * k[0] + k[1]) % 256**b == 27193 and (25888 * k[0] + k[1]) % 256**b == 11409:
            try:
                msg = block_decode(affine_decrypt(ciphertext, k, b), b)
            except:
                continue
            print(f'Problem 5: {msg}')
            print(f'Block : {b}')
            print(f'Key : {k}\n')

    # Problem 6
    ciphertext = [2881562576, 369203058, 73504835, 1526929104, 2259664109, 402991056, 
    422734829, 3748341712, 1688763471, 1447275245, 679140419, 2053553236, 39497061, 
    1068689747, 340791909, 301430236, 4281633534, 371419236, 144142198, 595585892, 
    1471070223, 2492642319, 4168374799, 3080192835, 2803641633, 2847978818, 2889054554, 
    2449609623, 333624642, 1327538857, 1231008783, 3288193056, 1240948649, 978641056, 
    304161744, 614863717, 1842205847, 4256050721, 1236027199, 3158610823, 430884691, 
    113709925, 177367294, 2319310642, 2675349195, 227891588, 4112117936]

    b = 4

    for end in range(256):
        last = 256**(b-1) * end
        # solve for lower mod system.

        gcd, x, y = egcd(last - block_encode('The ', 4)[0], 256**b)
        # need to divide out by the gcd
        # equation is then a*the + b = start
        #                  a*last + b = end
        # then we go to
        # a*(last - the) = end - start mod n
        mod = 256**b // gcd
        mult = ((last - block_encode('The ', 4)[0]) / gcd) % mod
        out = (ciphertext[-1] - ciphertext[0]) / gcd
        # so now its a * mult = out mod mod
        inverse = multiplicative_inverse(mult, mod)
        a_offset = (out * inverse) % mod
        k = [0, 0]
        msg = None
        for left in range(0, 256**b // mod):
            k[0] = int(left + a_offset)
            k[1] = (ciphertext[-1] - k[0] * last) % 256**b
            try:
                msg = block_decode(affine_decrypt(ciphertext, k, b), b)
                break
            except:
                continue
        if msg:
            print(f'Problem 6: {msg}')
            print(f'Block : {b}')
            print(f'Key : {k}\n')
            break
