
my_stu = [{'name': 'allen', 'age': 37, 'height': 182.0, 'scores': {'math': 89.0, 'english': 90.0, 'chemistry': 78.0}},
{'name': 'kate', 'age': 27, 'height': 180.0, 'scores': {'math': 89.0, 'english': 65.0, 'chemistry': 120.0}}]

print(my_stu[0])

print(my_stu[1])

print(my_stu[0]["name"])
print(my_stu[1]["name"])

print(my_stu[0]["scores"]["english"])
print(my_stu[1]["scores"]["chemistry"])