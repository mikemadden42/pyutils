#!/usr/bin/env python3

import keyword


def print_all_keywords():
    """
    Print the list of all Python keywords.

    This function uses the keyword module to retrieve the list of keywords
    in Python and prints them one by one.

    Returns:
        None
    """
    keywords_list = keyword.kwlist
    print("List of Python Keywords:")
    for kw in keywords_list:
        print(kw)


if __name__ == "__main__":
    print_all_keywords()
