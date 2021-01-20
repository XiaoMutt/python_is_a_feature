# one of python's aim is to write program like English, and python is not alone to have this aim.
# therefore, there are many operators in python that looks like English, such as "in", "not", "and"...
# these English-like logic operators allow expression to be written like English, but they also set up deadly traps.

print(True is not False)  # correct result, feels like English.

# the following English-like expression is very misleading
print(True is False is not True)  # TRAP: this returns False which is wrong.
# similarly
print(True is False is False)  # TRAP: this returns False which is wrong.

print(True is in [True, False])  # TRAP: you can use "is not" like in English doesn't mean you can use "is in"
print(True is not in [True, False])  # TRAP: you can not use "is not in", either

one = 1
print(one is 1 is True)  # TRAP: you will get SyntaxWaring and False
print(one == 1 is True)  # TRAP: you will get SyntaxWaring and False, this equals one==(1 is True)
print((one == 1) is True)  # correct
