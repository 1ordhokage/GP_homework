def sleight_of_hand(k: int, field: str) -> int:
    """Function that counts how many points can the players win.
    More info: README.MD
        Args:
            k (int): Number of keys that could be pressed by each player at the same time.
            field (str): String that consists ONLY of integers from 1 to 9 or dots.
        Returns:
            int: Number total of points.
        """
    nums = "123456789"
    nums_counter = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0
    }
    for i in field:
        if i in nums:
            nums_counter[i] += 1
    return sum(
        1
        for key, value in nums_counter.items()
        if 2 * k >= value > 0
    )


def main():
    """The main function."""
    k = int(input())
    field = ""
    for i in range(4):
        field += input().strip()
    print(sleight_of_hand(k, field))


if __name__ == "__main__":
    main()
