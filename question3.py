# Create a tuple containing names of sisters and brothers
sisters = ('Emily', 'Sophia')
brothers = ('James', 'Daniel', 'Matthew')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
num_siblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_name = 'John'
mother_name = 'Mary'
family_members = (father_name, mother_name) + siblings

# Print out the results
print("Siblings:", siblings)
print("Number of Siblings:", num_siblings)
print("Family Members:", family_members)
