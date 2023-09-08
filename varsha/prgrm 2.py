#PROGRAM TO FIND LEAP YEAR OR NOT 

def isLeapYear(year):
  if(year % 4 == 0 and year % 100 !=0)or year % 400 == 0:
    return True
  else:
   return False

year = int(input("ENTER A YEAR : "))

if isLeapYear(year):
  print("{} IS A LEAP YEAR.".format(year))
else:
  print("{} IS NOT A LEAP YEAR.".format(year))
  