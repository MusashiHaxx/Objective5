import time

def Countdown(T):
  print("T Minus {} to liftoff".format(T))
  for Cd in range(T-1,-1,-1):
    time.sleep(1)
    print(Cd)


Countdown(10)