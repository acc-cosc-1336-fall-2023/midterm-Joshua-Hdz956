def get_person_category(age):
    if age < 0:
        return ("Invalid Number")
    elif age >= 0 and age <= 1:
        return("Infant")
    elif age >1 and age < 13:
        return("Child")
    elif age >= 13 and age < 20:
        return("Teenager")
    elif age >= 20 and age <= 125:
        return("Adult")
    elif age > 125:
        return("Invalid Number")

def try_again():
    while True:
        z = input("Would you like to Try Again? y/n: ")
        if z == 'y' or z == "Y":
            run_main()
            break
        elif z == 'n' or z == 'N':
            print("Exiting")
            break
        else:
            print("Invalid, Select Y or N")

def run_main():
    while True:
        try:
            age = int(input("Enter Your Age: "))
            break
        except ValueError:
            print("NOT a whole number!")
    z = get_person_category(age)
    print(z)
    try_again()