"""
user_dictionary = {
    "username":"bhalaji@2003",
    "name":"Bhalaji C K",
    "age":21
}

# user_dictionary["married"] = True
print(len(user_dictionary))
print(user_dictionary.get("name"))

user_dictionary.pop("age")
print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)

for x,y in user_dictionary.items():
    print(x,y)

user_dictionary2 = user_dictionary
user_dictionary2.pop("age")
print(user_dictionary2)
print(user_dictionary)

del user_dictionary
"""

# Assingnmenet
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x,y in my_vehicle.items():
    print(x,y)

vehicle2 = my_vehicle.copy()

vehicle2["number_of_tyres"] = 4
print(vehicle2)

vehicle2.pop("mileage")
print(vehicle2)

print(my_vehicle)

