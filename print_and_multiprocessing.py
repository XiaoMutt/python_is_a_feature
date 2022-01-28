# If you use print and in multiprocessing, and your code is deadlocked for no reason, "print" may be the culprit.
# Try to use sys.stdout.write instead, or set PYTHONUNBUFFERED=1, or use python -u to start your script
