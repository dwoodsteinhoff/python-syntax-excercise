def print_upper_words(words):
    """
    Print each word in the list in all uppercase and on it's own line

        >>> print_upper_words(["make","me","all",""uppercase"])
        MAKE
        ME
        ALL
        UPPERCASE

    """

    for word in words:
        print(word.upper())

def print_e_words_upper_words(words):
    """
    Print each word in the list that starts with the letter e in all uppercase and on it's own line.

        >>> print_e_words_upper_words(["make","the","Elephant","and","eagle","words","uppercase"])
        ELEPHANT
        EAGLE
    """
    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())

def print_starts_with_upper_words(words,word_starts_with):
    """
        Print each word in the list that starts with a specific letter in all uppercase and on it's own line.

            >>> print_starts_with_upper_words(["hello","hey","goodbye","yo","yes"])
                                    word_starts_with={"h","y"}
            HELLO
            HEY
            YO
            YES
    """
    for word in words:
        for letter in word_starts_with:
            if word.startswith(letter):
                print(word.upper())
