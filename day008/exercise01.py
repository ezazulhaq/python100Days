# Create a function called greet()
def greet(name):
    print("Hello" + name)
    print("Hello" + name)
    print("Hello" + name)


greet('Ezaz')

# Create a function with more than 1 input


def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with_name('Ezaz', 'London')
greet_with_name(location='London', name='Ezaz')
