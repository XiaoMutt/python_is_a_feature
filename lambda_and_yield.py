
t = lambda a: str: str(a)

# yield converts a function to a generator
# can you create a generator using lambda and yield? seems logical

# f0=lambda: yield 1 # this is a wrong expression

f2 = lambda: (yield 1)  # TRAP: this will run,
# however, f2 is not a generator but a lambda function. calling f2 returns a generator which yields 1

f1 = lambda: (yield i for i in range(10))  # TRAP: this raises an runtime error but is caught by IDE

f3 = (lambda: (yield i) for i in range(10))  # TRAP: this creates a generator
# the outside () is the generator literal using the for comprehension. The generator yield ten lambda functions
# The then lambda functions upon calling returns a generator which yields a number.
# you can verify this by the following f4 which is a for comprehension
f4 = [lambda: (yield i) for i in range(10)]

# * key point: use generator literal directly; do not mix lambdas and yield *#
