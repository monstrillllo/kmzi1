from random import randbytes, randint, SystemRandom
from os import urandom
import math


def default_random(length: int = 100) -> bytes:
    return randbytes(length)


def crypto_random(length: int = 100) -> bytes:
    return urandom(length)


def generator(length: int = 100) -> list:
    res = []
    xt = SystemRandom().randrange(0, 9)
    xt1 = SystemRandom().randrange(0, 9)
    xt2 = SystemRandom().randrange(0, 9)
    for _ in range(length):
        x = (1176 * xt + 1476 * xt1 + 1776 * xt2) % (2 ** 32 - 5)
        xt2, xt1, xt = xt1, xt, x
        res.append(x.to_bytes(math.ceil(math.log2(x) / 8), 'big'))
    return res


def main():
    with open('./result1', 'wb') as file:
        file.write(default_random(200))
        # file.write(crypto_random(200))
        # file.write(generator(200))
        print('Done')
    # print(default_random(200))
    # print(crypto_random(200))
    # print(generator(200))


if __name__ == "__main__":
    main()

