"""
my_list = [1, 2, 3, 4, 5]

for item in range(3,6):
    print(item)

sum = 0
for item in my_list:
    sum += item
print(sum)

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for item in my_list:
    print(f"Happy {item}")
"""

# WhileLoop

"""
i = 0

while i < 5:
    i+=1
    if i % 2 == 0:
        break
    print(i)
"""

# Assignment
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
"""
for i in range(3):
    for item in my_list:
        if item == "Monday":
            continue
        print(f"Happy {item}")
    print(i)"""

i = 0
while i < 3:
    i+=1
    for item in my_list:
        if item == "Monday":
            print("-----")
            continue
        print(f"Happy {item}")