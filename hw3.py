age = float(input("how old are you"))
print(age)
if age > 19:
    print("adult")
else:
    if age < 1:
        print ("infant")
    elif 10 <= age <= 19:
        print("adolescent")
    else:
        print("child")
