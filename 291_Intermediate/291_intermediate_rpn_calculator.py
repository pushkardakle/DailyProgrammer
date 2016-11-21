from __future__ import division

import logging
import math
import re

""" Program to Calculate the calculation result for given Reverse Polish Notation(RPN) Expression """


class RPN_Calculator(object):
    """ Calculate result for given RPN expression """
    REMAINING_CHECK = re.compile(r' ')
    OPERATORS = r'\+\-\*\/\%\^'
    FACTORIAL_REPRESENTATION = re.compile(r'(\d+|\d+\.\d+) !')
    CALCULATION_REPRESENTATION = re.compile('(\d+|\d+\.\d+) (\d+|\d+\.\d+) ([' + OPERATORS + ']+)')

    def __init__(self, rpn_expression):
        self.rpn_expression = re.sub('\^', '**', rpn_expression)

    def calculate(self):
        """ Recursively calculate the result for given expression """
        if self.REMAINING_CHECK.search(self.rpn_expression) is not None:
            if self.FACTORIAL_REPRESENTATION.search(self.rpn_expression) is not None:
                self.rpn_expression = re.sub(self.FACTORIAL_REPRESENTATION,
                                             lambda x: str(math.factorial(int(x.group(1)))),
                                             self.rpn_expression, count=1)
            elif self.CALCULATION_REPRESENTATION.search(self.rpn_expression) is not None:
                self.rpn_expression = re.sub(self.CALCULATION_REPRESENTATION,
                                             lambda x: str(abs(eval(" ".join([x.group(1), x.group(3), x.group(2)])))),
                                             self.rpn_expression, count=1)
            else:
                logging.error("Invalid RPN Expression")
                return 1

            if self.REMAINING_CHECK.search(self.rpn_expression) is not None:
                self.calculate()
            else:
                logging.info("Calculation complete. The result is {}".format(self.rpn_expression))
                return 1


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s', level=logging.INFO)

    rpn_calc_obj = RPN_Calculator(rpn_expression="100 807 3 331 * + 2 2 1 + 2 + * 5 ^ * 23 10 558 * 10 * + + *")
    rpn_calc_obj.calculate()
