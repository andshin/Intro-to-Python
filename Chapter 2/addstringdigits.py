# let s be string with a sequence of numbers seperated by commas.
# s = '1.23, 2.4, 3.123, 5.33'
# write a program that sums of the numbers in s

s = '1.23, 2.4, 3.123, 5.33'
s = [x.strip() for x in s.split(',')]

x = 0
for i in s:
    x = x + float(i)
print (x)
