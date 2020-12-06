#factorial problem

#subroutine to work out the factorial of a number

def factorial(num):

  inp = num

  for Count in range(num-1,0,-1):
    num = num * Count

  print("{}! is: {}".format(inp,num))


number = int(input("Enter the number: "))

factorial(number)
