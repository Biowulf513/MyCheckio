import re

# my solution
def popular_words(text, words):
    words_array = {}
    for w in words:
        words_array[w] = len(re.findall(w, text.lower()))
    return words_array

# clear solution
# def popular_words(text, words):
    # res_dict = {}
    # new_text = text.lower()
    # for word in words:
    #     res_dict[word] = new_text.count(word)
    #
    # return res_dict

if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")