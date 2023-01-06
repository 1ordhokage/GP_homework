def to_binary(number: int) -> str:
    """Function that converts decimal number to binary.
        Args:
            number: Given integer.
        Returns:
            str: Binary representation of decimal integer.
    """
    res = ""
    prefix = "-" if number < 0 else ""
    number = abs(number)
    while number > 0:
        res += str(number % 2)
        number //= 2
    return prefix + res[::-1] if res else "0"


def main():
    print(to_binary(int(input())))


if __name__ == "__main__":
    main()
