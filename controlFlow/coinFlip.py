# Note: We will learn more about random and .randint() later in the chapter.

# All you need to know is that this program simulates a coin toss:

# ≈ 50% of the time, it's "Heads".
# ≈ 50% of the time, it's "Tails".


# Run the program 5 times to get a taste of the if/else statement!

# How many times did it go Heads?

# Write code below 💖
import random

num = random.randint(0, 1)   

if num > 0.5:
  print('Heads')
else:
  print('Tails')
