#!/usr/bin/python3
"""
Contains function that adds new attribute where possible
"""


def add_attribute(obj, attribute, value):
    """
    add attribute to object where possible
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
