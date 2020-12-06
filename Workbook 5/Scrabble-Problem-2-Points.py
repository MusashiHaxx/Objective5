#Scrabble problem 

#subroutine to calculate points

def point_cal(word):

  word = word.upper()

  pointscoring = ['E','A','I','O','N','R','T','L','S','U','D','G','B','C','M','P','F','H','V','W','Y','K','J','X','Q','Z']
  points = 0
  
  for x in range(0,len(word),1):

    pos = pointscoring.index(word[x])

    if pos >= 0 and pos < 10:
      points += 1

    elif pos >= 10 and pos < 12:
      points  += 2

    elif pos >= 12 and pos < 16:
      points += 3

    elif pos >= 16 and pos < 21:
      points += 4

    elif pos >= 21 and pos < 22:
      points += 5
    
    elif pos >= 22 and pos < 24:
      points += 8

    elif pos >= 24 and pos < 26:
      points += 10

  return points

      



    


#main program
word_to_score = input("Enter word: ")

points = point_cal(word_to_score)
print(points)