def gcd(a, b):
    if a > b:
        while b:
            a, b = b, a % b
        return a
    else:
        while a:
            b , a = a , b % a
        return b
