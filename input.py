name = input('enter your name here')
print(f'Hello {name}')

//it prompts the user to enter their name

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name
firstName = input('enter your name here')
distanceKm = input('how far is your destination?')
miles = float(distanceKm) / 1.609
print(f'Hello {firstName.title()} your distance {distanceKm} km is equivalent to {miles} miles')
