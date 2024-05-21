# Read the number of students from the user
N = int(input("Enter the number of students: "))

# Initialize an empty list to store weights in pounds
weights_lbs = []

# Read weights of N students into the list
for i in range(N):
    weight_lbs = float(input(f"Enter the weight of student {i+1} in pounds: "))
    weights_lbs.append(weight_lbs)

# Initialize an empty list to store weights in kilograms
weights_kgs = []

# Convert weights from pounds to kilograms and store them in the new list
for weight_lbs in weights_lbs:
    weight_kgs = weight_lbs * 0.453592  # 1 pound is approximately 0.453592 kilograms
    weights_kgs.append(round(weight_kgs, 2))  # Round the weight to two decimal places

# Print the lists
print("Weights in pounds:", weights_lbs)
print("Weights in kilograms:", weights_kgs)
