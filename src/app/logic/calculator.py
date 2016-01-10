"""Calcualtor module

This module contains calculator logic
"""

class Calculator:
    """Calculator class
    
    This class contains main logic 

    """

    def add(self, number1, number2):
        """
        The function for adding two numbers

        Args:
            param1 (real): the first number
            param2 (real): the second number

        Returns:
            real number which is result of addition

        >>> c = Calculator()
        >>> c.add(1, 2)
        3
        """
        return number1 + number2

if __name__ == '__main__':
    import doctest
    doctest.testmod()

