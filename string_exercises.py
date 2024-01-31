<<<<<<< HEAD
# Do not use reserved keywords for variable names

print("Hello World")


##### STRING SLICING #####
emp_name = "Jane Doe"
print(emp_name[2:6])
print(emp_name[:4])
print(emp_name[4:])
print(emp_name[-4:-1])
print(emp_name[1:6:2])

print(emp_name.count('e'))

print(emp_name.find('Doe'))

emp_name = (emp_name.replace('Jane', 'John'))
# Membership Test
print('oh' in emp_name)

#String Formatting
student_name = "Alice"
score = 87

print(student_name + ": " + str(score))
print("Name: {} \nScore: {}".format (student_name, score))
# f-strings
print(f'Name: {student_name} \nScore: {score}')
=======
# Do not use reserved keywords for variable names

print("Hello World")


##### STRING SLICING #####
emp_name = "Jane Doe"
print(emp_name[2:6])
print(emp_name[:4])
print(emp_name[4:])
print(emp_name[-4:-1])
print(emp_name[1:6:2])

print(emp_name.count('e'))

print(emp_name.find('Doe'))

emp_name = (emp_name.replace('Jane', 'John'))
# Membership Test
print('oh' in emp_name)

#String Formatting
student_name = "Alice"
score = 87

print(student_name + ": " + str(score))
print("Name: {} \nScore: {}".format (student_name, score))
# f-strings
print(f'Name: {student_name} \nScore: {score}')
>>>>>>> d889835ed4e1721c0d147e6435201e1b23b94fc6
print(f'10 times 3 is {10*3}')