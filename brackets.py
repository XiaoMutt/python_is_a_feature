################################
# () are the literal for tuple, but they have so many other usages which causes confusions and lead to traps.
################################

t0 = ()  # this creates an empty tuple
t1 = (1)  # TRAP: this equals t1=1 not a tuple
t2 = (1,)  # this creates a tuple of length 1
t3 = 1,  # TRAP: creates a tuple too; see "trailing_comma"
t4 = (1) * 8  # TRAP: this = 8 but not a tuple of eight 1s
t5 = (1,) * 8  # creates a tuple of eight 1s
t6 = 1, *8  # TRAP: will throw an error. IDE will not notify this error
t7 = (()) * 8  # TRAP: t7 is an empty tuple but a tuple of 8 empty tuples
t8 = ((),) * 8  # this creates a tuple of 8 empty tuples
t9 = ((1)) * 8  # TRAP: this equals 8 instead of a tuple of eight (1,) tuples
t10 = ((1,)) * 8  # TRAP: t10 is a tuple of eight 1s but a tuple of eight (1,) tuples
t11 = ((1,),) * 8  # this creates a tuple of eight (1,) tuples
# * The key point is to use comma to avoid ()'s function of group things *#

# * () is also used in the literal for generators (why? aren't there lambda expression? see lambda and yield section)
# * This makes things even more confusing and usages of () dangerous * #
t12 = (i for i in range(10))  # TRAP: this creates a generator but not a tuple of 0-9 elements; see below for {} and []

import numpy as np

np.array(i ** 2 for i in range(10))  # TRAP: this creates an array with 1 generator element in it.
np.argmax(i ** 2 for i in range(10))  # TRAP: this always return 0: it argmax from 1 generator element with index 0
np.array(range(10))  # OK

####
# {} are the literal for both dict and set
####
s0 = {}  # TRAP: s0 is a empty dictionary but a set. why can't {:} mean an empty dictionary?
s1 = {1}  # TRAP: s1 is a set
s2 = {i for i in range(10)}  # unlike (), this creates a set of 0-9
s3 = {(i for i in range(10))}  # TRAP: this creates a set of a generator; see above

#####
# []
#####

l0 = []  # this creates an empty list
l1 = [i for i in range(10)]  # unlike (), this creates an list of 0-9
l2 = [(i for i in range(10))]  # TRAP: this creates a list of a generator
l3 = [] * 8  # equals []
l4 = [[]] * 8  # trap a list of eight same list
l5 = [[] for _ in range(8)]  # correct way to create a list of eight different lists
l6 = [()] * 8  # this will create a list of eight empty tuples
l7 = [(1)] * 8  # this will create a list of eight 1s
l8 = [(1,)] * 8  # this will create a list of eight (1,) tuples
l9 = [1, ] * 8  # this will create a list of  eight 1s
