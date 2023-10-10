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