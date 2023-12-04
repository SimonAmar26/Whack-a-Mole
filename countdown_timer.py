import time

given_time = 90

for x in range(given_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    print(f"{minutes}:{seconds:02}")
    time.sleep(1)
print("Time's Up!")