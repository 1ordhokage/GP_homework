def largest_number(n: int, numbers: str) -> str:
    """Function that generates max number from given numbers (comparison sort).
        Args:
            n: Integer number of numbers from 1 to 100.
            numbers: Numbers.
        Returns:
            str: Max number from given numbers.
    """
    number_lst = numbers.split()
    for i in range(n):
        for j in range(i + 1, n):
            if number_lst[j] + number_lst[i] > number_lst[i] + number_lst[j]:
                number_lst[i], number_lst[j] = number_lst[j], number_lst[i]
    return "0" if number_lst == ['0'] * n else "".join(number_lst)


def main():
    print(largest_number(int(input()), input()))


if __name__ == "__main__":
    main()
