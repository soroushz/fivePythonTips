# Number 1:  normal loop
for i in [0,1,2,3,4]:
   print(i)

# range loop
for i in range(5):
   print(i)

# Using range with start, stop, and step arguments
for i in range(1, 10, 2):
   print(i)

# Number 2: Python default values in functions
def greet(name=None):
   if name is None:
       name = "Guest"
   print(f"Hello, {name}!")


def greet(name="Guest"):
   print(f"Hello, {name}!")


greet("Alice")
greet()

# Number 3: Python sublist extraction or Slicing
numbers = [0,1,2,3,4,5]
sliced = []
for i in range(1,4):
   sliced.append(numbers[i])
print(sliced)

print(numbers[1:4])

# Number 4: Enumerate
names = ['Alice', 'Bob', 'Charlie']
index = 0
for name in names:
   print(index, name)
   index += 1

for i, name in enumerate(names):
    print(i, name)

# Number 5: List comprehension
squares = []
for x in range(10):
   squares.append(x**2)
print(squares)

squares = [x**2 for x in range(10)]
print(squares)
