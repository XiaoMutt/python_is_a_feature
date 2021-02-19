# VARIABLE declaration and closure
# there are no variable declarations, variables are created on assignments
# therefore closure variables are immutable (unlike JavaScript)
glob = 1


def immutable_closure1():
    glob = 2  # created a new local variable glob
    print(glob)


def immutable_closure2():
    print(glob)  # this is closured glob


immutable_closure1()  # print 2
immutable_closure2()  # print 1


# all this causes confusion with variable scopes and setup many traps
# that's why it's better to shadow variable names
# To use variable at different scope, you need to use global and nonlocal keywords to do the "hack"
# and this is very hacky
# imagine you have a stack of nested function how will the variable scopes be?

def outside():
    global glob  # indicate glob is the global variable. you cannot use nonlocal because glob is at the module-level
    glob = 2  # change glob's value to 2
    print(glob)

    outside = 1  # trap: this created a new local variable with the same name as the function; better shadow it
    outvar = 1

    def inside1():
        global outvar  # trap: this will create a global variable outvar. correct: use nonlocal keyword
        outvar = 2
        print(outvar)
        global outside  # trap: this is the outside function; if you later change it's value, then the function is gone
        print(type(outside))

    def inside2():
        nonlocal outside2  # unlike the "global" keyword this will not create an outside2 variable, but raise an error
        outside2 = 1

    inside1()
    inside2()


# closure and the "self" keyword.
# The closured variable is immutable, and the self keyword is used to refer to the object itself (kind of, but not
# really, since it is passed in as a variable).
# when use self in closure it may create unexpected results.
from copy import deepcopy


class A(object):
    def __init__(self, fun):
        self.fun = fun


class B(A):
    def __init__(self, value):
        # self is set to the value when __init__ runs
        # it's not always pointing to the real self object. for example, when deepcopy is used.
        super(B, self).__init__(fun=lambda: self.value)
        self.value = value


b1 = B(1)
print(b1.fun())  # =1
b2 = deepcopy(b1)  # deepcopy: the self variable in the above lambda is still pointing to b1
b2.value = 2
print(b2.fun())  # =1
# use class methods instead of passing functions as variables
