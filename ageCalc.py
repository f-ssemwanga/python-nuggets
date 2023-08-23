import datetime
def calculateAge(year_of_birth):
  #takes a year of birth and calculates age
  currentYear = datetime.datetime.now().year
  try:
    age = currentYear- int(year_of_birth)
    return age
  except ValueError as err:
      return err
#print(calculateAge(1974))