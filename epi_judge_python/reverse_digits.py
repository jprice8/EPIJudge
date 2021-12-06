from test_framework import generic_test


def reverse(x: int) -> int:
    # result = 0
    # while x:
        # result = result * 10 + x % 10
        # x /= 10
    
    # return result

    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10

    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
