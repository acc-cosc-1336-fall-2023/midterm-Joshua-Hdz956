import question_a
print("We will determine whether you're an Infant, Child, Teenager, or Adult")
while True:
    while True:
        try:
            age = int(input("Enter Your Age: "))
            break
        except ValueError:
            print("NOT a whole number!")
    z = question_a.get_person_category(age)
    print(z)
    while True:
        y = input("Would you like to Try Again? y/n: ")
        if y == 'y' or y == "Y" or y == 'YES' or y =="yes":
            break
        elif y == 'n' or y == 'N' or y == 'NO' or y == 'no':
            print("Exiting")
            break
        else:
            print("Invalid, Select Y or N")
    if y == 'n' or y == 'N' or y =='NO' or y=='no':
        break