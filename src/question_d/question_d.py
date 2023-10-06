def get_day_of_week(day):
    if day < 1 or day > 7:
        return("Invalid Number")
    elif day == 1:
        return("Monday")
    elif day == 2:
        return("Tuesday")
    elif day == 3:
        return("Wednesday")
    elif day == 4:
        return("Thursday")
    elif day == 5:
        return("Friday")
    elif day == 6:
        return("Saturday")
    elif day == 7:
        return("Sunday")
    else:
        return("Invalid")



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
            day = int(input("Enter a Number of 1-7 for the day: "))
            break
        except ValueError:
            print("Not a WHOLE Number")
    y= get_day_of_week(day)
    print(y)
    try_again()