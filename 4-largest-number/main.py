def largest_number(n: int, numbers: str) -> str:
    number_lst = numbers.split()
    for i in range(n):
        for j in range(i + 1, n):
            if number_lst[j] + number_lst[i] > number_lst[i] + number_lst[j]:
                number_lst[i], number_lst[j] = number_lst[j], number_lst[i]
    return "".join(number_lst)


def main():
    print(largest_number(int(input()), input()))


if __name__ == "__main__":
    main()
