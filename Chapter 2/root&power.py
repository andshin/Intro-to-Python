# Write a program that asks user to enter an integer and prints two integers 
# root and pwr such that 0 < pwr < 6 and root ** pwr is equal to the integer entered by user.
# if no such pair exists, it should print a msg to that effect.


num = int(input("Enter a postive integer nubmer: "))
root = 0
pwr = 0

for i in range(1,num):
    if i == 0:
        continue
    root = i
    for x in range(1,num):
        pwr = x
        if root**pwr == num:
            print(str(root) + "^" + str(pwr) + " = " + str(num))
            break
    if root**pwr == num:
        break
if root**pwr != num:
    print("none")

