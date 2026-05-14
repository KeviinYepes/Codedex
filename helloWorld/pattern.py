# Suppose we want the output to look exactly like this pattern below:

#        1
#      2 3
#    4 5 6
# 7 8 9 10

# How can you do that?

# Create a pattern.py program that prints this pattern exactly as shown.

# This will likely take some trial and error, but give it a shot!


# Start counting from 1, since this is the first number in the pattern.
number = 1


for row in range(1, 5):
    spaces = "  " * (4 - row)
    print(spaces)
    line = spaces
    for col in range(row):
        line += str(number) + " "
        number += 1
    print(line.rstrip())
