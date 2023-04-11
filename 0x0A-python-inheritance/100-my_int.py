#!/usr/bin/python3
"""
Contains class MyInt that inherits from int
Sneaky --> has == and != operators inverted!
"""


class MyInt(int):
    """
        __init__(self, num)
        __eq__(self, otr)
        __ne__(self, otr)
    """
    def __init__(self, num):
        """initialize num"""
        self.num = num

    def __eq__(self, otr):
        """
        Return:
           True if both not equal
        """
        return self.num != otr

    def __ne__(self, otr):
        """
        Return:
           True if both equal
        """
        return self.num == otr
