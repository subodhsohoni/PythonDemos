# Define a variable (add) that represents a statement that can take arguments (n, m). 
# This variable is linked to the statement n + m using the lambda keyword which represents a lambda function
add = lambda n, m: n + m

subtract = lambda n, m: n - m

# Call the lambda function using the variable name as if that is a function and pass the arguments to it
print(add (5, 3))
print(subtract(5, 3))