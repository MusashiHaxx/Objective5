#counter-controlled iterations

#subroutine to demonstrate loops
def OutputMessage(Message):
  for counter in range (0,20,1):
    print(Message)

#main program
Message = "This is how you get code to repeat"
OutputMessage(Message)
