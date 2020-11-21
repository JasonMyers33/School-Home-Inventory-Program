#------------------------------------------------------------------------
# Program Name: Home Inventory Program
# Program Author: Jason Myers
# Program Objective: Create a home inventory class that will be used by a
#                       National Builder to maintain inventory of available
#                       houses in the country.  
#-----------------------------------------------------------------------
# Pseudocode:
#           Create a dictionary for the homes
#           Private fuctions for:
#                               Square Feet
#                               Address
#                               City
#                               State
#                               Zip Code
#                               Model Name
#                               Sale Status only options are:
#                                           sold, available, under contract
#           Methods to include:
#                               constructor
#                               add a new home
#                               remove a home
#                               update home attributes
#                               view inventory on screen
#                               output all home inventory to a CSV file.
#------------------------------------------------------------------------
# Program Inputs: dictionary, home parts - address, squarefeet, city, state
#                   zip code, model name, sale status
# Program Outputs: Print dict. export to CSV.
#------------------------------------------------------------------------

import csv # Will print file to CSV
home = {} # Dictionary 
homekey = 0 # Indexing variable  for homes
status = ('Sold', 'Available', 'Under contract') # Variable to handle home status

class HomeInventory:
  def __init__(self):
    self._squarefeet = 0
    self._address = ''
    self._city = ''
    self._state = ''
    self._zipcode = 0
    self._modelname = ''
    self._salestatus = '' 
  
  # Home update and add both call this function. Saves lines and reduces error potential.
  def combine(self):
    while True: # Home address checks for blanks.
      _address = input('Enter the address of the home: ')
      if _address != "":
        break
      else:
        print('\nThe address cannot be blank\n')
    while True: # Home City checks for blanks.
      _city = input('Enter the city where the home resides: ')
      if _city != "":
        break
      else:
        print('\nThe City cannot be blank\n')
    while True: # Home State checks for blanks.
      _state = input('Enter the state where the home resides: ')
      if _state != "":
        break
      else:
        print('\nThe State cannot be blank\n')
    while True: # Home zip code checks for numbers and 5 digits long.
      try:
        _zipcode = int(input('Enter the zip code where the home resides: '))
        if len(str(_zipcode)) != 5: # Checking for 5 digits
          print('\nThe zip code needs to be 5 digits long.\n')
        else:
          break
      except: # Error handling if entry is text
        print('\nThe zip code cannot contain any letters.\n')
    while True: # Square feet checks for numbers.
      try:
        _squarefeet = int(input('Enter squarefeet of the home: '))
        break
      except: # Error handling if entry is text
        print('\nPlease enter the square feet as a number.\n')
    while True: # Home model checks for blanks.
      _modelname = input("Enter the home's model name: ")
      if _modelname != "":
        break
      else:
        print('\nThe model cannot be blank\n')  
    while True: # Home status checks that the entry matches the status variable.
      _salestatus = input('Enter current status of the home (Sold, Available, Under Contract): ')
      _salestatus =_salestatus.capitalize() # Capitalizing the entry for looks and searching
      if any(s in _salestatus for s in status):
        break
      else:
        print('\nPlease enter "Sold," "Available," or "Under Contract" \n')
    home[self] = (_address, _city, _state, _zipcode, _squarefeet, _modelname, _salestatus)

# Add a home
  def add(self):
    global homekey # Using homekey to index the key value for each home.
    homekey += 1
    HomeInventory.combine(homekey)

# Delete a home
  def delete(self):
    for key in sorted(home.keys()): # Printing the homes to make it easy to select what to delete.
      print('\nHouse position %s: %s' % (key, home[key]))
    while True:
      try:
        delete = int(input('\nWhat house position do you want to delete? '))
        home.pop(delete)
        print('\nThe home has been deleted.\n')
        break
      except KeyError: # Handeling the errors
        print('\nThat position is not not found.\n')
      except ValueError: # Handeling the errors
        print('\nEnter the House position number.\n')

# Update a home
  def update(self):
    for key in sorted(home.keys()): # Printing the homes to make it easy to select what to update.
      print('\nHouse position %s: %s' % (key, home[key]))
    position = int(input('\nWhat house position do you want to update? '))
    if position in home.keys():
      HomeInventory.combine(position)
    print('Home record updated.\n')
  
# Print the dictonary to a CSV file
  def f(self):
    name = input('Enter a file name: ')
    name = name + '.csv' # Adding .csv to make csv file
    with open (name, 'w') as file:
      file.write('Home Position,Address,City,State,Zip code,Square feet,Model,Sale Status'+'\n')
      for key in home.keys():
        file.write('%s, %s\n'%(key, home[key]))
      file.close()
      print('\nRecord saved.\n')
    
# Menu system
while True:
  try:
    print('1. Create a record for a new home.')
    print('2. Update an existing home record')
    print('3. Remove a home record')
    print('4. View inventory')
    print('5. Save inventory to a file')
    print('6. Exit the program')
    print('\n')

    # Options for the menu
    option = int(input('Select a menu option: '))
    if option == 1:
      HomeInventory.add(input)
      print('\n')
    elif option == 2:
      HomeInventory.update(input)
      print('\n')
    elif option == 3:
      HomeInventory.delete(input)
      print('\n')
    elif option == 4:
      for key in sorted(home.keys()):
        print('\nHouse position %s: %s\n' % (key, home[key]))
    elif option == 5:
      HomeInventory.f(input)
      print('\n')
    elif option == 6:
      print('\nThank you.\n')
      break
    else: # Handling  wrong number errors
	    print('\nThat is not a valid option. Please try again.\n')
  except: # Handling alpha entry error
    print('\nThat is not a valid option. Please try again.\n')
