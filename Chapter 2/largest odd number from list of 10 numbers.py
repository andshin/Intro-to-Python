#book page 20

#write a program that asks the user to input 10 integeres, 
#and the nprints the largest odd number that was entered.
#if no odd nubmer entered it should print a msg to that effect.
print("You will be asked to enter 10 numbers")
x = 0
oddcheck = 0

n1 = int(input("Enter the first nubmer: "))
if n1 != 0 and n1 > x:
    x = n1
else:
    oddcheck += 1
    
n2 = int(input("Enter the second nubmer: "))
if n2 != 0 and n2 > x:
    x = n2
else:
    oddcheck += 1
    
n3 = int(input("Enter the third nubmer: "))
if n3 != 0 and n3 > x:
    x = n3
else:
    oddcheck += 1
    
n4 = int(input("Enter the forth nubmer: "))
if n4 != 0 and n4 > x:
    x = n4
else:
    oddcheck += 1

n5 = int(input("Enter the fifth nubmer: "))
if n5 != 0 and n5 > x:
    x = n5
else:
    oddcheck += 1

n6 = int(input("Enter the sixth nubmer: "))
if n6 != 0 and n6 > x:
    x = n6
else:
    oddcheck += 1

n7 = int(input("Enter the seventh nubmer: "))
if n7 != 0 and n7 > x:
    x = n7
else:
    oddcheck += 1

n8 = int(input("Enter the eigth nubmer: "))
if n8 != 0 and n8 > x:
    x = n8
else:
    oddcheck += 1

n9 = int(input("Enter the ninth nubmer: "))
if n9 != 0 and n9 > x:
    x = n9
else:
    oddcheck += 1

n10 = int(input("Enter the tenth and last nubmer: "))
if n10 != 0 and n10 > x:
    x = n10
else:
    oddcheck += 1

if oddcheck == 10:
    print("Why didn't you enter any odd numbers")
else:
    print("Largest odd number is " + str(x))
