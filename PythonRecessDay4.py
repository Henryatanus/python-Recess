# Dictionaries
# creating and using dictionaries
# dictionary methods and operations
"""_summary_
    Dictionaries in python are collection of keys and values
    - ordered
    -mutable
    and indexed by keys
    
    """
    # Example 1: create a dictionary for a student pursuing software engineering , the key must be your name,age,technology interest and year of study put your own details
student_dict={
    'fname':'Jonathan',
    'age': 49,
    'technology': 'AI and Mi',
    'course':"BSE",
    'year':'2'
    

    }
print(student_dict['age'])
print(student_dict['technology'])
print(student_dict['year'])
print(student_dict['fname'])
# Access values
# modify values
# Exercise 1 Modify age and technology

a=student_dict['course']= 'Civil'
student_dict['age']= '17'
print(student_dict['age'])
student_dict['technology']= 'Structural enginering'
print(student_dict['technology'])
print("Student name is: "+student_dict['fname']+" persuing "+student_dict['course'])

# Adding keys and values
student_dict['email']='atanuscalcbee@gmail.com'


# Exercise 2: Remove a key and value from student dictionary

del student_dict['year']
print(student_dict)

# Common Dictionary methods
"""summary
get() // returns the value for the specified key if the key is in the dictionary
if not it returns the default value

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and return the corresponding value



"""
# Example 3: Use the get method to get the value

print(student_dict.get('technology'))

# Exercise 3: Use the update method to change value in age 

student_dict.update({'fname': 'Atanus'})
print(student_dict)

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary

if 'age' in student_dict:
    print(" present age", student_dict['age'])
    
else:
    print("Infinity or less")
    
print()

# keys(), values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""summary

keys() returns a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and
values tuple pairs

 """
 
 # Exercise : Use the update method to change the course and add a new 
 # key "WhatsApp_Number" to the dictionary
 
student_dict.update({
    'course': 'Architecture',
    'WhatsApp_Number': '0705186568'
})
print(student_dict)
print()