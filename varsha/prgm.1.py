#IMPLEMENT A RECURSIVE FUNCTION TO CALCULATE THE FACTORIAL OF A GIVEN NUMBER

def fact_rect(n):
  if n==0 or n==1:
    return 1
  else:
     return n*fact_rect(n-1)
          
number=int(input(" ENTER A VALUE : "))
res=fact_rect(number)
          
print(" THE FACTORIAL OF {} is {}".format(number,res))