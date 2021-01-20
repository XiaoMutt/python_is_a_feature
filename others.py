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
