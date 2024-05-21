it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update({'LinkedIn', 'Netflix', 'Uber'})
print("Added it_companies:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Netflix')
print("Removed it_companies:", it_companies)

print("Difference between remove and dicard:")
print("remove(): Raises KeyError if the element doesn't exist in the set")
print("discard(): Doesn't raise any error if the element doesn't exist")

# Print the updated it_companies set before deletion
print("Updated it_companies:", it_companies)

# Join A and B
joined_set = A.union(B)

# Find A intersection B
intersection_set = A.intersection(B)

# Is A subset of B
is_subset = A.issubset(B)

# Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)

# Join A with B and B with A
joined_AB = A.union(B)
joined_BA = B.union(A)

# Symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)

# Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
length_age_list = len(age)
length_age_set = len(age_set)

# Print out the results
print("Joined set of A and B:", joined_set)
print("Intersection of A and B:", intersection_set)
print("Is A subset of B:", is_subset)
print("Are A and B disjoint sets:", are_disjoint)
print("Joined A with B:", joined_AB)
print("Joined B with A:", joined_BA)
print("Symmetric difference between A and B:", symmetric_difference)
print("Length of age list:", length_age_list)
print("Length of age set:", length_age_set)
