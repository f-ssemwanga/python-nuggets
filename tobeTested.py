import datetime
def ageCalc(year_of_birth):
  #takes a year of birth and calculates age
  currentYear = datetime.datetime.now().year
  age = currentYear- year_of_birth
  return age

print(ageCalc(1974))