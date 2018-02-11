def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    first = text.find(symbol) + 1
    second = text[first:].find(symbol)

    if second < 0:
        return None
    else:
        # print (first + second)
        return first + second


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

# second_index("sims", "s")
# second_index("find the river", "e")
# second_index("hi", " ")
# second_index("hi mayor", " ")
# second_index("hi mr Mayor", " ")
# second_index("see you", "e")