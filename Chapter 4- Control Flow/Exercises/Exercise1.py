#Exercise 1: Names :ballot_box_with_check:
'''Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the aliens color is green. If it is, print a message that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)'''

alien_color = input("Enter color : ")
if alien_color == "green":
    print("Congrats! You have earned 7 points!")
elif alien_color == "red":
    print("sorry! You have earned 0 points")
else:
    exit