#FizzBuzz Problem

#subroutine to fizzbuzz

def Fizzbuzz(num_max):

  for x in range (1,num_max,1):

    if x % 3 == 0 and x % 5 == 0:

      print("FizzBuzz")

    elif x % 5 == 0:
      print("Buzz")

    elif x % 3 == 0:
      print("Fizz")

    else:
      print(x)


#main program

max  = int(input("Enter the maximum number: "))

Fizzbuzz(max)