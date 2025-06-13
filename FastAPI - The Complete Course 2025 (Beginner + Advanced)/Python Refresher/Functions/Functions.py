

"""def my_function():
    print("Inside my_function")

my_function()"""

"""def print_my_name(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

print_my_name("Bhalaji","C K")"""

"""def print_color_red():
    color = "Red"
    print(color)

color = "Blue"
print(color)
print_color_red()"""

"""def print_numbers(hig , low):
    print(hig)
    print(low)

print_numbers(low=10,hig=3)"""

"""def multiply(a, b):
    return a*b

solution = multiply(2, 3)
print(solution)"""

"""def pirnt_list(list_of_number):
    for x in list_of_number:
        print(x)

numbers = [1, 2, 3, 4, 5]
pirnt_list(numbers)"""

"""def buy_item(cost_of_item):
    return cost_of_item + add_tax(cost_of_item)

def add_tax(cost_of_item):
    current_tax = .03
    return cost_of_item * current_tax

fianl_cost = buy_item(50)
print(fianl_cost)"""

# Assignment

def user_detail(first_name, last_name,age):
    create_user_dictionary = {
        "firstname":first_name,
        "lastname":last_name,
        "age":age
    }
    return create_user_dictionary


solution = user_detail("bhalaji", "c K", 28)
print(solution)