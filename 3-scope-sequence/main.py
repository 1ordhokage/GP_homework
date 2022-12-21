import constant


def find_opening_brace(sequence: list[str]) -> tuple[int, int]:
    """Function that finds the opening brace index to be replaced.
        Args:
            sequence: Scope sequence.
        Returns:
            tuple[int, int]: Index of opening brace to be replaced and weight.
    """
    # difference between numbers of opening and closing braces
    weight = 0
    index = len(sequence) - 1
    for i in range(index, -1, -1):
        weight += -1 if sequence[i] == ")" else 1
        if sequence[i] == "(" and weight < 0:
            index = i
            break
    return index, weight


def lexicographically_minimal(
        sequence: list[str],
        n: int,
        index: int,
        weight: int
) -> list[str]:
    """Function that makes sequence's suffix lexicographically minimal.
        Args:
            sequence: Scope sequence.
            n: Half the number of source sequence length.
            index: Opening brace index to replace.
            weight: Difference between numbers of opening and closing braces.
        Returns:
            list[str]: Sequence with lexicographically minimal suffix.
     """
    for i in range(index + 1, 2 * n):
        opening_brace_condition = i <= (2 * n + index + weight) / 2
        sequence[i] = "(" if opening_brace_condition else ")"
    return sequence


def get_next_sequence(sequence: list[str], n: int) -> list[str]:
    """Function that generates next scope sequence in lexicographical order.
        Args:
            sequence: Scope sequence.
            n: Half the number of source sequence length.
        Returns:
            list[str]: Next scope sequence in lexicographical order.
    """
    opening_brace_index, opening_brace_weight = find_opening_brace(
        sequence
    )
    sequence[opening_brace_index] = ")"
    return lexicographically_minimal(
        sequence,
        n,
        opening_brace_index,
        opening_brace_weight
    )


def psp(n: int) -> str:
    """Function that generates scope sequences in lexicographical order.
        Args:
            n: Half the number of source sequence length.
        Returns:
            str: Scope sequences in lexicographical order.
    """
    scope_sequences = "(" * n + ")" * n
    current_scope_sequence = list(scope_sequences)
    for _ in range(constant.CATALAN_NUMBERS[n] - 1):
        current_scope_sequence = get_next_sequence(current_scope_sequence, n)
        scope_sequences += "\n" + "".join(current_scope_sequence)
    return scope_sequences


def main():
    print(psp(int(input())))


if __name__ == "__main__":
    main()
