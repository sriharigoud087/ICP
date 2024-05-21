# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Golden'
dog['breed'] = 'Retriever'
dog['legs'] = 4
dog['age'] = 5

# Create a student dictionary and add key-value pairs
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# Get the length of the student dictionary
student_length = len(student)

# Get the value of skills and check the data type
skills_value = student['skills']
skills_data_type = type(skills_value)

# Modify the skills values by adding one or two skills
student['skills'].extend(['HTML', 'CSS'])

# Get the dictionary keys as a list
student_keys = list(student.keys())

# Get the dictionary values as a list
student_values = list(student.values())

# Print out the results
print("Dog Dictionary:", dog)
print("Student Dictionary Length:", student_length)
print("Skills Data Type:", skills_data_type)
print("Modified Skills:", student['skills'])
print("Dictionary Keys:", student_keys)
print("Dictionary Values:", student_values)
