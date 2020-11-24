# Define a dictionay of keys and values (strings at this time) 
persons = {"First":"Subodh", "Next":"Gouri"}
# Add another key - value pair to the dictionary
persons["Last"] = "Mahesh"
# Create a list of names (strings)
trainers = ["Subodh", "Gouri", "Mahesh", "Ravi"]
# Add another key value (list) pair to the dictionary 
persons["trainers"] = trainers
# Print the entire dictionary
print("Entire Dictionary:")
print(persons)
# Print the entire list which is part of the dictionary
print("List in the Dictionary:")
print(persons["trainers"])
# Print only first item in the list which is part of the dictionary 
print("First item in the list in the Dictionary:")
print(persons["trainers"][0])
# Print only some items in the list which is part of the dictionary
print ("Only some items in the list which is part of the dictionary")
for index in range(1,len(trainers) -1):
    print(persons["trainers"][index])