# function and variables are treated as the same in class: they are all attributes
# in addition, classes are dynamic:
#   - they are loaded as needed, no compiles, so circular typing will not work
#   - you can add and delete their attribute at any time
#   - so they are not real class which is a data type and should be static
#   - instead, they are more like a hashmap/dictionary object simulating type and inheritance
# the classmethod, staticmethod, property decorator use __get__, __set__ to trigger values replacement at class level
#   - they only work on attributes defined at class level
# lambda function cannot access class variables in class definition
# all of these cause unexpected behavior of type checking and runtime errors

class Attr(object):
    def __init__(self, fun):
        self.fun = fun


class A(object):
    _next: A  # error, cannot do typing of a type that is has not finished defining: use "A"

    @staticmethod
    def helper():
        print("helper")

    error = Attr(A.helper())  # error: cannot use the function in defining class either
    good = Attr(lambda: A.helper())  # but you can use the function indirectly by putting it in a lambda

    FIRST = 1
    SECOND = FIRST + 1  # FIRST can be accessed here
    print_first = lambda: print(FIRST)  # cannot access FIRST; no closure?
    print_a_first = lambda: print(A.FIRST)  # should use A.FIRST

    nice_property = property(lambda self: "nice property")  # will work

    def __init__(self, next_: "B"):  # error: B is not defined yet, you cannot use B in type, use "B" instead
        self._next = next_
        self.value = B.value  # but you can use B here, because when __init__ runs B has been defined
        self.wrong_property = property(lambda _: "this will not work: property added in an instance")

        first = 1
        self.print_first = lambda: print(first)

    @property
    def next(self):
        return self._next

    @staticmethod
    def check_tuple_length(self, t: tuple):
        return len(t)

    @classmethod
    def decor(cls):
        return lambda x: x

    @decor()  # the decor property can be used as decorator in the same class definiation
    def to_be_decorred(self):
        pass


class B(A):
    __slots__ = ['next']  # this will override the next property without an error thrown
    value = 1

    @decor  # wrong: decor cannot be found, though B is a subclass of A
    @A.decor()  # use A.decor
    def to_be_decorred_too(self):
        pass
