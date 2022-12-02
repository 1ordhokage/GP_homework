def dists_to_left_zero(len_array: int, array: list[str]) -> list[int]:
    """Function that counts distances from houses to the nearest left empty area.

    Args:
        len_array (int): Length of the given array.
        array (list[str]): List of house numbers. Zero is for empty area.

    Returns:
        list[int]: Array of distances to the nearest left empty area.
    """
    dist_arr = []
    curr_dist = len_array

    for elem in array:
        if elem == "0":
            curr_dist = 0
        else:
            curr_dist += 1
        dist_arr.append(curr_dist)

    return dist_arr


def nearest_zero(len_array: int, array: str) -> str:
    """Function that counts distances from houses to the nearest empty area.
    Args:
        len_array (int): Length of the given array.
        array (str): Str of house numbers separated by whitespaces.
         Zero is for empty area.

    Returns:
        str: Array of distances to the nearest empty area.
    """
    nums = array.split()
    arr_of_left_dists_to_zero = dists_to_left_zero(len_array, nums)
    arr_of_right_dists_to_zero = dists_to_left_zero(len_array, nums[::-1])[::-1]
    return " ".join(
        str(
            min(
                arr_of_left_dists_to_zero[i],
                arr_of_right_dists_to_zero[i]
            )
        ) for i in range(len_array)
    )


def main():
    """The main function."""
    house_nums_str = input()
    print(
        nearest_zero(
            len(house_nums_str.split()),
            house_nums_str
        )
    )


if __name__ == "__main__":
    main()
