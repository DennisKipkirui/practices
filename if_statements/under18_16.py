# Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, display the message “You can lern to drive”, if they are 16, display the message “You can buy alottery ticket”, if they are under 16, display the message “You can go Trickor-Treating”. 

age = int (input("what is your age?"))
if age >= 18:
    print ("You can vote")
elif age == 17:
    print ("You can lern to drive")
elif age == 16:
    print ("You can buy alottery ticket")
else:
    print("You can go Trick-or-Treating")
