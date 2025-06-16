"""
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.append(6)
print(my_list)

my_list.insert(2, 7)
print(my_list)

my_list.remove(6)
print(my_list)

my_list.pop(0)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

"""
"""
people_list = ["Bhalaji", "Dharun", "Pradhiba"]
print(people_list[-3])  

print(people_list[1:3]) 
"""

# Assingment
"""
--Create a list of 5 animals called zoo
--Delete the animal at the 3rd index.
--Append a new animal at the end of the list
--Delete the animal at the beginning of the list.
--Print all the animals
--Print only the first 3 animals
"""
zoo = ["dog", "cat", "cow", "goat", "hen"]
print(zoo)

zoo.remove(zoo[2])
print(zoo)

zoo.append("duck")
print(zoo)

zoo.pop(0)
print(zoo)

print(zoo[0:3])
