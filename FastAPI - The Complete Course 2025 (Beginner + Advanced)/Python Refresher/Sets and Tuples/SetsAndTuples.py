"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

# Sets

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)

print(len(my_set))

for x in my_set:
    print(x)

my_set.discard(1)
print(my_set)

my_set.clear()
print(my_set)

my_set.add(6)
print(my_set)

my_set.update({1, 2, 3})
print(my_set)

# Tuples

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

print(len(my_tuple))

print(my_tuple[1])

