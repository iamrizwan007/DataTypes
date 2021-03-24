d = eval(input("Enter dictionary"))
sum = 0
for k,v in d.items():
 sum = sum + int(v)
print("The sum of values is: ",sum)

def inbuilt():
 print(sum(d.values()))