#ASCII Art Problem

#subroutine to convert string to ASCII Art]

def ASCII_Art(string):

  string_len = len(string)
  print( "+-" * string_len)

  for x in range(0, string_len , 1):
    print("|{}".format(string[x]),end ="",flush= True)
  
  print("\n")
  print( "+-" * string_len, flush = False)


ASCII_Art("Computer Science.")