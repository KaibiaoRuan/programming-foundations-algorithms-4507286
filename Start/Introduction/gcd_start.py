# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    if a >= b:
        r = a % b
        print(f"Computing GCD of {a} and {b}, remainder is {r}")
        if r == 0:
            return b
        elif r == 1:
            return None
        return gcd(b, r)
    else:
        return gcd(b, a)


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
