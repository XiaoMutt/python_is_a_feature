# indent using mixture of space and tab will cause problem if you are not using an IDE
# type the following into a python console, and it will raise run time error
for i in range(10):
    j = i + 1  # the indent is 4 space
    print(j)  # the indent is 1 tab


# underscore
# underscore is wildly used in python. Using underscore to separate words is pythonic
# this leads to very long names and uncomfortable typing experience caused by underscore (pressed by the pinky finger)
def get_dict_of_a_to_b():
    a_to_b = dict()
    return a_to_b


# changing iterable object while iterating lead to unexpected results
# runtime error occur if change set or dictionary keys while iterating, but not for list
s0 = set(range(10))
for n in s0:
    s0.remove(n)  # runtime error: set size change

d0 = dict({i: i for i in range(10)})
for k, v in d0.items():
    d0.pop(k)  # runtime error

l0 = list(range(10))
for n in l0:
    print(n)
    l0.remove(n)  # no runtime error: lead to unexpected result
    # if use append, then the for loop never ends

# r strings which treats \ as backslash but not an escape command
# however does it?
print(r'\a\b\c')  # this works

# add the backslash at the end will not work
print(r'a\b\c\') # this is an error because of the last backslash
