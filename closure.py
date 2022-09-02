# Python Closure Trap:
# when nested function access variables of an outer function and the nested function got returned by the outer
# function, the accessed variables will form closure in the nested function.
# However, this does not work in the following example, when the outer function returns a list of nested functions:

def this_does_not_work():
    res = []
    for c in "abcdefg":
        char = c

        def fun():
            print(char)

        res.append(fun)
    return res


funs = this_does_not_work()
for f in funs:
    f()


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

# following pass the value of c to char and the closure works:

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
