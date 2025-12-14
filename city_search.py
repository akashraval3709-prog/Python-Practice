# Program: Check City Availability
# Author: Akash Raval
# Purpose: Check if a specific city exists in the list using 'in' operator

# Create a list of available cities
cities = ['Surat', 'Ahmedabad', 'Rajkot', 'Baroda']

# Take city name input from the user
value = input('Enter your cities name :')

# Logic: Use 'in' operator to check existence
# This checks if the 'value' is present inside the 'cities' list
if value in cities:
    print('Yes, Available')
else:
    print('Not, Available')
