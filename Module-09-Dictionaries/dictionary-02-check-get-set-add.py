# Dictionary
# length (len), check a key, get, set, add

# Dictionary 1 -------------------------------------------
print(" Dictionary with string keys ".center(44, "-"))
dict_employee_IDs = {"ID01": 'John Papa',
                     "ID02": 'David Thompson',
                     "ID03": 'Terry Gao',
                     "ID04": 'Barry Tex'}
print(dict_employee_IDs)

# len -------------------------------------------
print(" dictionary length ".center(44, "-"))
dict_employee_IDs_length = len(dict_employee_IDs)
print(str(dict_employee_IDs_length))

# Check if a key is in dictionary -------------------------------------------
print(" Check if a key is in dictionary ".center(44, "-"))
emp_id = "ID02"
# emp_id = "ID05" # Invalid Key
if emp_id in dict_employee_IDs:
    name = dict_employee_IDs[emp_id]
    print('Employee ID {} is {}.'.format(emp_id, name))
else:
    print('Employee ID {} not found!'.format(emp_id))

# Dictionary 2 -------------------------------------------
print(" Dictionary with string keys ".center(44, "-"))
dict_employee1_Info = {"Name": 'John Papa',
                       "Department": 'Network',
                       "DataOfBirth": '02/24/1975',
                       "Salary": '$60K US'}
print(dict_employee1_Info)

# get -------------------------------------------
print(" Getting data from dictionary ".center(44, "-"))
name = dict_employee1_Info.get("Name")
department = dict_employee1_Info.get("Department")
dob = dict_employee1_Info.get("DataOfBirth")
salary = dict_employee1_Info.get("Salary")

print('{} works in {} department with a salary of {}. His data of birth is {}'.format(name, department, salary, dob))
print(dict_employee1_Info.get("City"))
print(dict_employee1_Info.get("Branch", "Unknown"))

# set -------------------------------------------
print(" Setting value for an item in dictionary ".center(60, "-"))
dict_employee1_Info["Department"] = 'Development'
dict_employee1_Info["Salary"] = '$70K US'
print('{} works in {} department with a salary of {}. His data of birth is {}'.format(name, department, salary, dob))
department = dict_employee1_Info.get("Department")
salary = dict_employee1_Info.get("Salary")
print('{} works in {} department with a salary of {}. His data of birth is {}'.format(name, department, salary, dob))

print(dict_employee1_Info)

# add -------------------------------------------
print(" Add to dictionary ".center(60, "-"))
dict_employee1_Info["Branch"] = "Airport Branch"
dict_employee1_Info["City"] = "Boston"
print(dict_employee1_Info)
print(dict_employee1_Info.get("City"))
print(dict_employee1_Info.get("Branch", "Unknown"))