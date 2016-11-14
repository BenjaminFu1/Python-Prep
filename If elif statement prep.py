#This is my fortune telling program
import random
import time
answer= random.randint(1,6)
print("\nWelcome to my fortune telling program\n")
print("I am going to choose a number between 1-6 for you")
time.sleep(3)
print("Your number is:",answer"\n")
if answer == 1:
        print("You will make a new friend this week")
elif answer == 2:
        print("You will do well in your GCSEs")
elif answer == 3:
        print("You will find something you thought you'd lost")
elif answer == 4:
        print("You will get a credit this week")
elif answer == 5:
        print("You will get a girl friend this month")
else:
        print("You will find a 50 pounds note on the floor this month")
