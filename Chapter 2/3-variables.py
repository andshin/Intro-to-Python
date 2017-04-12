# Page 16. Finger exercise.
# Write a program that examines x,y,z and prints the largest odd nubmer among them. If none of them are odd, print some msg.

x,y,z = 2,54,1
a,b,c,k = 0,0,0,0

if x % 2 != 0:
    a = x
else:
    k += 1
    
if y % 2 != 0:
    b = y
else:
    k += 1

if z % 2 != 0:
    c = z
else:
    k += 1

if k == 3:
    print("none of them are odd numbers !")
else:
    print(max(a,b,c))
