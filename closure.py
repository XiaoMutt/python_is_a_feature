# Python Closure Trap:
# when nested function access variables of an outer function and the nested function the accessed variables will form
# closure in the nested function.
# However, since python variables are not declared explicitly, a closure variable is readonly and its scope is unclear,
# which leads to serious bugs.

def wrapper():
    c = 1

    def good():
        print(c)  # closure: no problem

    def wrong():
        print(c)  # error: c is not assigned (see next line)
        c = 2  # closured variable c cannot be changed. This is declaring c new variable c in the local scope.
        print(c)

    def ok():
        nonlocal c  # make it work by telling Python the c variable is not in the localscope
        print(c)
        c = 2
        print(c)


# What if the variable c is changing? Will its value get "closured"?
# Actually not in the following case:
def this_does_not_work():
    res = []
    for c in "abcdefg":
        char = str(c)  # make a new variable char out of c for every loop

        def fun():
            print(char)

        res.append(fun)
    return res


funs = this_does_not_work()
for f in funs:
    f()  # print all "g"s


# Is this a bug of Python?
# In Kotlin this works perfectly fine.
# fun outer(): ArrayList<() -> Unit> {
#     val res = arrayListOf<() -> Unit>()
#     for (c in arrayOf('a', 'b', 'c', 'd', 'e', 'f', 'g')) {
#         fun nested(): Unit {
#             println(c)
#         }
#         res.add(::nested)
#     }
#     return res
# }
#
# fun main() {
#     val funs = outer()
#     for (f in funs) {
#         f()
#     }
# }

# To make it work in python, pass c to a function as an argument:
def this_works():
    res = []
    for c in "abcdefg":
        def generate_fun(char):
            def fun():
                print(char)

            return fun

        res.append(generate_fun(c))
    return res


funs = this_works()
for f in funs:
    f()


# Closure in class declaration
# See also classes_and_typing.py
def fun(data):
    class A:
        data = data  # error: variable data is declared in the class A scope, then try to assign its value to itself

    class B:
        data_ = data  # change variable name then it works.
