import question_a
try_again = 'y'
while try_again == 'y' or try_again == 'Y' or try_again == 'yes' or try_again == 'YES':
    while True:
        try:
            age = int(input("Enter Your Age: "))
            break
        except ValueError:
            print("NOT a whole number!")
    z = question_a.get_person_category(age)
    print (z)
    try_again = str(input("Enter 'Yes' or 'Y' if you would like to Try Again: "))
    if try_again == 'y' or try_again == 'Y' or try_again == 'YES' or try_again == 'yes':
        print("\nYou selected to try again!")
    else:
        print("Exiting Program")
            