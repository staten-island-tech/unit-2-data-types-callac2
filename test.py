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
if int(number_1 and number_2) > 0:
    for i in range(1, number_1 and number_2 + 1):
      if number_1 and number_2 % i == 0:
        if number_1 % i == 0:
            if number_2 % i == 0:
             print(i) """

""" 
C = "c"
e = "."
def occupied_places(x,y,t):


    for i in range(x):
        if(y[i] == "c" and t[i] == "c"):
                found += 1
    print(found)
occupied_places(5,"ccccc","ccccc") """

""" def which_language(x,t,s):

    t = "T"
    s = "S"
    s = 0
    t = 0

    letter = str(input("enter text here:"))
for letter in range(input): 
       
        if letter.lower() == "s":
            s += s+1
            
        if letter.lower() == "t":
            t += t+1
            
            if s >= t:
                print("French")
        elif s<= t:

            print ("English")

             """
""" def numberhoni(word):
    count = 0
    state = 0
    for char in word:
        if state == 0 and char.upper() == "H":
            count = 1
        elif state == 1 and char.upper() == "O":
            count = 2
        elif state == 2 and char.upper() == "N":
            count = 3
        elif state == 3 and char.upper() == "I":
            count += 1
            state = 0


    print (count)
    print(state)
numberhoni("HONIHONI") """

def gamble_input(quarter, machine_1, machine_2, machine_3,turns):   
    quarter = 0
    m1=machine_1
    m2=machine_2
    m3=machine_3
    turns = 0


while quarter >= 1:
    quarter = quarter - 1
    if m1 == 0:
        turns = turns + 1
    if turns == 35:
        turns = 0
        quarter = quarter + 30
    

    else:
        if quarter!=1:
            turns+=1
        
        if m2 % 100 == 0:
            quarter+=59
            turns+=1
        else:
            quarter!=1
            turns+=1
        
        if m3 % 10 ==0:
            quarter+=8
            turns+=1
        else:
            quarter!=1
            turns+=1
        print(turns)
gamble_input(48,[3,10,4])
print(f'Martha plays {turns} times before going broke. :C')

    







    

