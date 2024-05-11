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

if __name__ == "__main__":
    assert egcd(1234,567) == (1, -17, 37)
    assert egcd(256, 33) == (1, 4, -31)
    assert egcd(2024, 748) == (44, -7, 19)