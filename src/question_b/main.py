import question_b

print('Celsius\t Fahrenheit')
C=0
while C <= 20:
    F = question_b.get_fahrenheit(C)
    print(C,'\t',F)
    C += 1