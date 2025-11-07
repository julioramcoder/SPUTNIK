### Ask the user for the starting number ###

start = int(input("Enter the starting number for the countdown: "))

### Countdown using a while loop ##
while start > 0:
    print(start)
    start -= 1  # Decrease the number by 1

print("Countdown finished!")
