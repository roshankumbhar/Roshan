# This is my main code file
"""

comments ddddddddddddddddddddddddddddddd
 ddddddddddddddddd
 ddddddddddddddddd

"""
import logging

name = 'roshan'
age = 30
case = 12

print(f"my name is {name} and "
      f"my age is {age}")

print('my name is %s and my age is %s'
      % (name, age))

print('my name is %s' % name)

logging.basicConfig(level=logging.INFO)
logging.info('Test %s %s',
             case, age)

logging.info('my name is %s',
             name)
