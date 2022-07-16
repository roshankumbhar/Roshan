'''
This program adds two numbers and displays their results
'''

import logging

A = 1
B = 2
print('Sum of Numbers:', A + B)
print(f'Total of Numbers: {A + B}')
print(f'Addition of Numbers: {A + B}')
print(f"A is {A} and B is {B}")

NAME = 'roshan'

logging.basicConfig(level=logging.INFO)
logging.info('my name is %s%%',
             NAME)


NAMES = ['Roshan', 'Govind', 'Kumbhar']
N = '\n'.join(NAMES)
print(f"Winners are :\n{N}")
