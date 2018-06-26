#!/usr/bin/env python3

import re


def match_a_number(num=None):
    """
    Check if your 10-digit number matches
    """
    num_regex = re.compile(r"\d\d\d\d\d\d\d\d\d\d")
    num_object = num_regex.search(num)
    if num_object:
        print("Your input, {}, matches the regex.".format(num))
    else:
        print("Your input, {}, does not match the regex.".format(num))


match_a_number("0123456789")
match_a_number("abcdefghij")
match_a_number("012fdaf4gad")