import datetime
def calculateAge(year_of_birth):
  #takes a year of birth and calculates age
  currentYear = datetime.datetime.now().year
  try:
    if year_of_birth:
      age = currentYear- int(year_of_birth)
      return age
    else:
      return 'Please enter a number'
  except ValueError as err:
      return err
#print(calculateAge(1974))