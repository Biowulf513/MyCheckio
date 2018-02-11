def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # print(text)
    # print(begin, end)
    #=============Best solution=============

    # start = text.find(begin) + len(begin) if begin in text else None
    # finish = text.find(end) if end in text else None

    # return text[start:finish]
    # =============My solution==============
    parameters = [begin, end]
    position = [0, 0]
    for p in range(0,2):
        try:
            position[p] = text.find(parameters[p])
        except Exception:
            position[p] = None
        else:
            position[p] = text.find(parameters[p])

        if position[p] < 0:
            position[p] = None

    if position[0] != None:
        position[0] += len(begin)

    return text[position[0]:position[1]]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

# between_markers('What is >apple<', '>', '<')
# between_markers("<head><title>My new site</title></head>","<title>", "</title>")
# between_markers('No[/b] hi', '[b]', '[/b]')
# between_markers('No [b]hi', '[b]', '[/b]')
# between_markers('No hi', '[b]', '[/b]')
# between_markers('No <hi>', '>', '<')
# print('Wow, you are doing pretty good. Time to check it!')