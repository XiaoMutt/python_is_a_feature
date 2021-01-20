# function and variables are treated as the same in class: they are all attributes
# in addition, the attributes of classes are dynamic: you can add and delete at any time
# looks like that the classes are simulated and they are more like a hashmap/dictionary object
# all of these cause unexpected behavior of type checking and runtime errors

class Attr(object):
    def __init__(self, fun):
        self.fun = fun


class A(object):
    _next: A  # error, cannot do typing of a type that is has not finished defining

    @staticmethod
    def helper():
        print("helper")

    error = Attr(A.helper)  # error: cannot use the function in defining class either
    good = Attr(lambda: A.helper())  # but you can use the function indirectly by putting it in a lambda

    def __init__(self, next: B):  # error: B is not defined yet, you cannot use B in type
        self._next = next
        self.value = B.value  # but you can use B inside the functions

        # because variable b is assigned in __init__
        # the following will not trigger an type check error (as least in PyCharm)
        # but will raise an run time exception
        self.a = self.b
        self.b = 1

    @property
    def next(self):
        return self._next

    @staticmethod
    def check_tuple_length(self, t: tuple):
        return len(t)


class B(A):
    __slots__ = ['next']  # this will override the next property without an error thrown
    value = 1

