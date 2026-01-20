Test file for print_square function.

>>> print_square = __import__('4-print_square').print_square

>>> print_square(4)
####
####
####
####

>>> print_square(10)
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########

>>> print_square(0)


>>> print_square(1)
#

>>> print_square(2)
##
##

>>> print_square(3)
###
###
###

>>> print_square(5)
#####
#####
#####
#####
#####

>>> try:
...     print_square(-1)
... except Exception as e:
...     print(e)
size must be >= 0

>>> try:
...     print_square(-10)
... except Exception as e:
...     print(e)
size must be >= 0

>>> try:
...     print_square(2.5)
... except Exception as e:
...     print(e)
size must be an integer

>>> try:
...     print_square(-2.5)
... except Exception as e:
...     print(e)
size must be an integer

>>> try:
...     print_square("4")
... except Exception as e:
...     print(e)
size must be an integer

>>> try:
...     print_square([1, 2, 3])
... except Exception as e:
...     print(e)
size must be an integer

>>> try:
...     print_square(None)
... except Exception as e:
...     print(e)
size must be an integer

>>> try:
...     print_square(True)
... except Exception as e:
...     print(e)
size must be an integer

>>> try:
...     print_square(False)
... except Exception as e:
...     print(e)
size must be an integer

>>> try:
...     print_square()
... except Exception as e:
...     print(type(e).__name__ + ":", e)
TypeError: print_square() missing 1 required positional argument: 'size'
