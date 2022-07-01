"""Calculator"""

# Either import module
from calc import *

a = int(input("Enter First Number: "))
b = int(input("Enter second Number: "))

add_result = add(a, b)
print(add_result)

sub_result = sub(a, b)
print(sub_result)

mul_result = mul(a, b)
print(mul_result)

div_result = div(a, b)
print(div_result)
