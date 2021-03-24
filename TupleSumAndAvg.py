t = eval(input("Enter the numbers in tuple format '(10,20,30)' separated by ,: "))
sum = 0
avg = 0.0
for x in t:
 sum = sum + x
print("sum of tuple is :",sum)
print("avg of tuple is :",sum/len(t))