import question_d
print("We will determine the day of the week, from the numbers 1-7.")
try_again = 'y'
while try_again == 'y' or try_again == 'Y' or try_again == 'yes' or try_again == 'YES':
    while True:
        try:
            day = int(input("Enter a Number of 1-7 for the day: "))
            break
        except ValueError:
            print("Not a WHOLE Number")
    z = question_d.get_day_of_week(day)
    print (z)
    try_again = str(input("Enter 'Yes' or 'Y' if you would like to Try Again: "))
    if try_again == 'y' or try_again == 'Y' or try_again == 'YES' or try_again == 'yes':
        print("\nYou selected to try again!")
    else:
        print("Exiting Program")
        