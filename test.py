""" x = 3
y = float(3)
print(x,y)

 """
""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """
""" 
def discount(age, Member, Resident):
    
    if age <= 12 or age >= 65:
        print("Discount applicable!")

    elif Member == True:
        print("Discount applicable!")
    elif Resident == True:
        print("Discount applicable!")
    else:
        print("No Discount Applicable, Sorry!")
discount(11, False, False) """


""" values = [1,2.23,6,7,2,30,15]
print(values)
print(values[1])
print(values[3])
         """

""" "test"
["t","e","s","t"]
print(["t","e","s","t"][1]) """

""" x = "this is a thing"
y= x.split( )
z = y[1]
print(y)
print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" 
x = "test"
y = "tEsT"
print(f"yay {y}")
 """

""" temp = 68
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" thenumber = int(input("Enter a number: "))
if int(thenumber) % 2 == 0:
        print("even")
else:
        print("odd")
 """
""" service = input("How was the service? (Bad, Okay, Good, Great) ")
bill_value = float(input("Enter bill amount: "))
if service == "Bad":
    print(bill_value * 0)
elif service == "Okay":
    print(bill_value * 0.15)
elif service == "Good":
    print(bill_value * 0.20)
elif service == "Great":
    print(bill_value * 0.25) """

""" number = int(input("Enter a number to get its factors: "))
if int(number) > 0:
    for i in range(1, number + 1):
        if number % i == 0:
            print(i) """

""" number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if int(number_1) > 0:
    print("These are the common factors. The GCF is the largest one.")
    for i in range(1, number_1 + 1):
        if number_1 % i == 0:
            if number_2 % i == 0:
             print(i) """
