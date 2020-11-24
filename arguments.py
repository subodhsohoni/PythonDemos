import sys
# Print all the arguments
print ("Arguments list:{}", str(sys.argv))
#Print only 2nd argument. Catch exception if there is no second argument
try:
    print (sys.argv[2])
except IndexError:
    print ("Second argument not found")
else:
    print ("Done")
