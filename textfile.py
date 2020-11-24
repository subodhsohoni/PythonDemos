# Open a text file in read mode
trainers_file = open(file="mydata.txt", mode="r")
# Read all the lines in the file and print those on the screen
trainers = trainers_file.read()
print(trainers)

# Open a text file in write mode
subjects_file = open(file="subjects.txt", mode="w")
# Create a list that is to be written in the file
subjects = [".NET", "Java", "C#", "Python"]
# For each item in the list, write a line in the the file
for subject in subjects:
    subjects_file.writelines(subject)
    subjects_file.writelines("\n")

# Open the same file in the append mode
subjects_file = open(file="subjects.txt", mode="a")
# Write a string at the end of the file
subjects_file.write("JavaScript")