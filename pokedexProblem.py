# Since 1996, the Pokémon video game franchise has delighted players around the world with collectible pocket monsters. A Pokédex is a device that tracks the information for Pokémon that are seen or caught.

# Create a new file called pokedex.py.

# Next, let's define a Pokemon class with the following attributes:

# entry (integer)
# name (string)
# types (list of strings)
# description (string)
# is_caught (boolean)
# Note: Make sure to use the __init__() method.

# Next, create an instance method called .speak() that prints a string of the sound a Pokémon makes. A Pokémon usually just says their name, so make the .speak() simply print out their name twice!

# Then, create another instance method called .display_details() that prints the attributes of a Pokemon object like the following:

# Entry Number: 25
# Name: Pikachu
# Type: Electric
# Description: It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
# Pikachu has already been caught!

# Lastly, create three Pokemon class objects and use the .speak() or .display_details() instance methods for each one.

# For more information about any Pokémon you want to add, see the Pokédex!

# Are you ready to earn the next badge?

# Bonus: For all the super fans, try and add more attributes to the Pokemon class definition, like level, region, height, or weight.




# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught =  is_caught
    
  def speak(self):
    print(f"{self.name}  {self.name}!!")

  def display_details(self):
    print(f"""Entry number: {self.entry} 
    Name: {self.name}
    Type: {self.types}
    Description: {self.description}
    """)

pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)
charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)
gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'], 'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', False)

pikachu.speak()
charizard.speak()
gyarados.speak()
pikachu.display_details()
charizard.display_details()
gyarados.display_details()



