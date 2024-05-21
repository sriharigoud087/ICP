ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sorting the list and finding the min and max age
sorted_ages = sorted(ages)
min_age = sorted_ages[0]
max_age = sorted_ages[-1]

print("Sorted Ages:", sorted_ages)
print("Min Age:", min_age)
print("Max Age:", max_age)

# Adding the min and max age again to the list
ages.append(min_age)
ages.append(max_age)

print("Updated Ages with Min and Max Age:", ages)

# Finding the median age
sorted_ages_len = len(sorted_ages)
middle_index = sorted_ages_len // 2

if sorted_ages_len % 2 == 0:  # Even number of ages
    median_age = (sorted_ages[middle_index - 1] + sorted_ages[middle_index]) / 2
else:  # Odd number of ages
    median_age = sorted_ages[middle_index]

print("Median Age:", median_age)

# Finding the average age
average_age = sum(ages) / len(ages)
print("Average Age:", average_age)

# Finding the range of ages
age_range = max_age - min_age
print("Age Range:", age_range)
