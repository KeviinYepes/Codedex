# Let's put our newfound knowledge of the from and as keywords to the test by finding out the surface areas of the planets in our solar system! 🪐

# Create a new file called solar_system.py.

# Next, import the following at the top of the file:

# From the math module, the pi (π) variable.
# From the random module, the .choice() method, renamed as ch for short.
# Then, copy and paste the following list:

# planets = [
#   'Mercury',
#   'Venus',
#   'Earth',
#   'Mars',
#   'Saturn'
# ]

# Next, use the ch() method to get a random string from planets and assign it to a variable called random_planet.

# And use the imported pi (π) variable to calculate the surface area of a sphere:


# area=4πr 
# 2
 

# To do this, we'll need to know the radius r for a given random_planet (rounded to the nearest kilometer).

# Write an if/elif/else statement and assign a value to r with the following in mind:

# If random_planet is 'Mercury', then r is 2440.
# Else, if random_planet is 'Venus', then r is 6052.
# Else, if random_planet is 'Earth', then r is 6371.
# Else, if random_planet is 'Mars', then r is 3390.
# Else, if random_planet is 'Saturn', then r is 58232.
# Else, print "Oops! An error occurred." to the console.
# Lastly, calculate the area and print the name of the random_planet along with its area to the console.

# Bonus: The calculated results may seem a bit long. Is there a built-in Python function that can round it?


# Solar System 🪐
# Codédex

from math import pi; from random import choice as ch

planets = [
 'Mercury',
 'Venus',
 'Earth',
 'Mars',
 'Saturn'
]

random_planet = ch(planets)
radius = 0

if random_planet == 'Mercury':
  radius = 2440
elif random_planet == 'Venus':
  radius = 6052
elif random_planet == 'Earth':
  radius = 6371
elif random_planet == 'Mars':
  radius = 3390
elif random_planet == 'Saturn':
  radius = 58232
else:
  print('Oops! An error occurred.')

planet_area = 4 * pi * radius * radius

print(f'Area of {random_planet}: {int(planet_area)} sq mi')