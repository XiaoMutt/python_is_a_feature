# traps of string break and trailing comma

# raw string and backslash;
# see https://docs.python.org/3/reference/lexical_analysis.html; Quote:
# Even in a raw literal, quotes can be escaped with a backslash, but the backslash remains in the result;
# this leads to confusions:

# this is wrong: print(r"abcde\")
print(r"abcde\\")  # prints abcde\\
print(r"abcde\"")  # prints abcde\"
# however this is wrong: print(r"abcde\\"")
print(r"abcde\\""")  # prints abcde\\

# string concatenation in brackets mixed with trailing comma
# normal string tuple
t0 = ("tuple of 1 of 2",
      "tuple of 2 of 2")

# trailing comma is OK
t1 = ("tuple of 1 of 2",
      "tuple of 2 of 2. trailing comma is OK",)

# if missing a comma in parentheses then the strings are concatenated automatically, t2 is a string
t2 = ("forgot the comma"
      "your got a string accidentally")

# if you accidentally have another trailing comma at the end, then t2 is still a tuple, but with wrong data
t3 = ("forgot the 1st comma"
      "but with a trailing comma. gives a different tuple",)



