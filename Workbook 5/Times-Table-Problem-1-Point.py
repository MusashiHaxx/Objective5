#times table problem

#subroutine to output the x times table
def TimesTable(X):
  for Counter in range(1,13):
    print("{} x {} = {}".format(Counter,X,Counter * X))

 
timestable = int(input("Enter your times table: "))
TimesTable(timestable)