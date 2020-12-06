#passcode problem


#subroutine to generate password form two words.

def password_maker(word1,word2):

  word1 = word1.lower()
  word2 = word2.lower()
  vowels = ['a','e','i','o','u']
  password = ''

  for x in range(0,len(word1),1):
    try:
      vowels.index(word1[x])
      pass_num_temp = x
      pass_num_temp = str(pass_num_temp)
      password = password + pass_num_temp

    except:
      password = password

  for x in range(0,len(word2),1):
    try:
      vowels.index(word2[x])
      pass_num_temp = x
      pass_num_temp = str(pass_num_temp)
      password = password + pass_num_temp

    except:
      password = password

  return password



#main program

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
password = password_maker(word1,word2)
print("Your password is {}.".format(password))

