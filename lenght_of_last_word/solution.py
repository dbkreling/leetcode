#!/usr/bin/python

# My solution
s = "   This is an example of a string   "

st = s.strip()
words = st.split()
print(len(words[-1]))

# In one line:
print("In one line:")
print(len(s.strip().split()[-1]))

# Optimized (from answers)
s = s.split()
print(len(s[-1]))