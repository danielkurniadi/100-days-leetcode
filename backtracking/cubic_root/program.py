import math


def cubicRoot(x, err=0.0001):
    if x == 0 : return 0
    xn = x // 4
    xn1 = (2 * xn + x / (xn * xn)) / 3.0
    while abs(xn1 * xn1 * xn1 - x) > err:
            xn = xn1
            xn1 = (2 * xn + x / (xn * xn)) / 3.0
    return xn1


if __name__ == "__main__":
    print(cubicRoot(9, 0.001))
    print(cubicRoot(120, 0.001))
