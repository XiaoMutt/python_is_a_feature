# Python's built-in modules are global (not under python...), and Python need to load some modules when starts.
# This makes it easy to pollute the built-in modules with your own. E.g.
# Create an empty file named types.py in the out-most folder, and then run any other scripts in your project.
# See what will happen: Python will try to load types from your types.py file and fails.
