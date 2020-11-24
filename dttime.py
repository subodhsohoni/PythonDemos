from datetime import datetime, timedelta
# Create a variable for date-time for now
rightnow = datetime.now()
# Convert the datetime to string and print
print (rightnow.strftime("%m-%d-%Y %H:%M:%S"))
# Remove one day from rightnow variable and assign the value to another variable
yesterday = rightnow + timedelta(days = -1)
# Convert the datetime of new vaiable to string and print
print (yesterday.strftime("%m-%d-%Y %H:%M:%S"))