import time

#Given time is noted in seconds.
given_time = 90

#Used a for loop to get a repeat appearance of decreasing time.
for x in range(given_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    print(f"{minutes}:{seconds:02}")
    time.sleep(1) #Added with intention of making the print("Time's Up!") appear one second after the countdown timer ended.

#Used print() to make a message to users that their time has ended.
print("Time's Up!")
