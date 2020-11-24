# Create a list
trainers = ["Subodh", "Gouri", "Mahesh", "Ravi"]
# Iterate within the list using For loop
for EachTrainer in trainers:
    print (EachTrainer)
print ("\n")
# Extend the list by adding another list to it
trainers.extend(["Manish", "Saket"])
# Sort the list in place
trainers.sort()
count = 0
# Iterate within the sorted list using While loop
while (count < len(trainers)):
    print (trainers[count])
    count = count + 1
print ("Done")
# Remove an item from the list
trainers.remove("Manish")
# Add another item to the list (duplicate)
trainers.append("Mahesh")
# Output all items in the list
print(trainers)
# Count of an item in the list
print(trainers.count("Mahesh"))
# 0 based Index of an item appearing first time in the list
print(trainers.index("Mahesh"))
# List 2nd to 4th item in the list (0 based)
print (trainers[1:3])
# list all items from 3rd item in the list
print (trainers[2:])
