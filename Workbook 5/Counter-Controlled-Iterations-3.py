#counter controlled iterations

#subroutine to demonstrate loops
def CharLoop(Message):
  for Index in range(0,len(Message),1):
    Alpha = Message[Index]
    Alpha = Alpha.lower()
    if Alpha == "a" or Alpha == "e" or Alpha == "e" or Alpha == "i" or Alpha == "o" or Alpha == "u":
      print("Charatcer {} of {} is a vowel".format(Index,Message))

    

#main program

Message = "Should indexes start at 0 or 1? The compromise of 0.5 was rejected without proper consideration."

CharLoop(Message)