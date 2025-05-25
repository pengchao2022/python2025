
#列表里嵌套字典

students = [{'name': 'allen', 'age': 88.0, 'height': 99.0, 'scores': {'math': 67.0, 'english': 56.0, 'chemistry': 78.0}}]

print(students[0]["name"])

print(students[0]["scores"]["math"])

print(students[0]["scores"]["chemistry"])