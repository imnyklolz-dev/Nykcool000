my_dict = {1: "apple", 2: "ball"}

my_dict = {"name": "John", 1: [2, 4, 3]}

my_dict = {"name": "Jack", "Age": 26}

print(my_dict["name"])
print(my_dict["Age"])

my_dict["Age"] = 27
print(my_dict)

my_dict["Address"] = "Downtown"
print(my_dict)

my_dict.pop("Age")
print(my_dict)

my_dict["Address"] = "Uptown"
print(my_dict)

my_dict.clear()
print(my_dict)