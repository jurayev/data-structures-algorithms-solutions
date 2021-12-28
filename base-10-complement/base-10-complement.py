def calculate_bitwise_complement(n):
    """
    0 ^ 0 = 0
    1 ^ 1 = 0
    0 ^ 1 = 1

    """

    left = n
    k_bit_set = 1
    while left > 0:
        left >>= 1
        print(bin(n), bin(k_bit_set))
        n ^= k_bit_set

        k_bit_set <<= 1

    return n


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()