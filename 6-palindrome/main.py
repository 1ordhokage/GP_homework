class MyStack:
    """Stack implementation."""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def prepare_phrase(phrase: str) -> list:
    """Function that clears symbols from the phrase except letters and numbers.
        Args:
            phrase: Given phrase.
        Returns:
            list: Cleared phrase in lowercase.
    """
    return list(
        filter(
            lambda x: x.isalnum(), 
            phrase.lower()
        )
    )    


def push_first_half(phrase: list, palindrome_stack: MyStack):
    """Function that pushes the first half of the phrase to the stack.
        Args:
            phrase: Given phrase.
            palindrome_stack: Stack for palindrome checking.
    """
    end_index = len(phrase) // 2
    for symbol in phrase[:end_index]:
        palindrome_stack.push(symbol)
    

def check_second_half(phrase: list, palindrome_stack: MyStack) -> bool:
    """Function that compares symbols from
        the second half of phrase with the stack symbols.
        Args:
            phrase: Given phrase.
            palindrome_stack: Stack for palindrome checking.
        Returns:
            bool: The result of comparison.
    """
    start_index = len(phrase) - len(phrase) // 2
    for symbol in phrase[start_index:]:
        if palindrome_stack.pop() != symbol:
            return False
    return True


def palindrome_checker(phrase: str) -> bool:
    """Function that checks if the given phrase is palindrome.
        Args:
            phrase: Given phrase.
        Returns:
            bool: Is the given phrase a palindrome.
    """
    phrase = prepare_phrase(phrase)
    palindrome_stack = MyStack()
    push_first_half(phrase, palindrome_stack)
    return check_second_half(phrase, palindrome_stack)


def main():
    print(palindrome_checker(input()))


if __name__ == "__main__":
    main()
