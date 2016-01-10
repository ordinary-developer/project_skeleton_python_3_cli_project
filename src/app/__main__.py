# -*- coding: utf-8 -*-
"""Main application module

   here all invockable application logic is situated

"""

from logic.calculator import Calculator


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.add(1, 2))
