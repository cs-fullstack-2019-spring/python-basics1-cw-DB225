def main():
    problem1()
    problem2()
    problem3()
    problem4()

#Create ca function with two variables.
# One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.
def problem1():
    first = "My name is: "
    second = "Didier"
    print(first+second)
###############################################################
#Create a function to ask the user to enter the extra credit they earned.
# If they entered less than 5 print “That’s not enough extra credit.”
# If they entered more than 20 print “That’s too much extra credit”.
def problem2():
    extraCredit = int(input("Enter the extra credit you earned: "))
    if(extraCredit < 5):
        print("That's not enough extra credit.")
    elif(extraCredit > 20):
        print("That’s too much extra credit.")
    else:
        print(" ")
###############################################################
#Create a function to ask a user to enter a password.
# Enter a password. Ask user to reenter password.
# Check to see if they are correct.
def problem3():
    EnterPassword1 = input("Enter a password: ")
    EnterPassword2 = input("Enter the password again: ")
    correctPassword = "DB225"

    if(EnterPassword1 != correctPassword or EnterPassword2 != correctPassword):
        print("That's not correct")
    elif(EnterPassword1 == correctPassword and EnterPassword2 == correctPassword):
        print("CORRECT")
    else:
        print(" ")
###############################################################
#Create a function to ask for two card numbers.
# If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”
def problem4():
    card1 = int(input("Put the first card number: "))
    card2 = int(input("Put the second card number: "))
    sumcards = card1+card2

    if(sumcards == 21):
        print("BLACKJACK!")
    elif(sumcards > 21):
        print("BUST!")
    elif(sumcards < 21):
        print("The total is "+sumcards)
    else:
        print(" ")
###############################################################
if __name__ == '__main__':
    main()