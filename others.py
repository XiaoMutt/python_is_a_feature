# indent using mixture of space and tab will cause problem if you are not using an IDE
# type the following into a python console, and it will raise a run time error
for i in range(10):
    j = i + 1  # the indent is 4 space
    print(j)  # the indent is 1 tab


# underscore
# The underscore is wildly used in python. Using underscores to separate words is pythonic.
# This leads to very long names and uncomfortable typing experience caused by underscore (pressed by the pinky finger)
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
    # if append is used here, then the for loop never ends

# The datetime format bug.
# The %Y of the datetime format should represent a four-digit year (padded with 0 if necessary).
# However, this is not true for all platforms. Probably depends on the backend C implementation.
# This causes unexpected error when talking to other systems. E.g. frontend using the dayjs package
from datetime import datetime

datetime_year = datetime.strptime("0001", "%Y")  # parse the string year to datetime.
string_year = datetime_year.strftime("%Y")  # format back to string: this becomes "1" in some platforms.
print(string_year)

# Use * as a spead operator in the for comprehension is an error
items = [[1, 2, 3], [4, 5, 6]]
# flattened = [*item for item in items]  # error
flattened2 = [i for item in items for i in items]  # instead use 2 for comprehensions
