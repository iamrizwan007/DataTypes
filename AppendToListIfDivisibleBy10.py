a,b = input("Add number to the list in range of a to b that are divisible by 10 separated by space\n>> ").split()
l = []
for i in range(int(a),int(b)+1):
 if i%10==0:
  l.append(i)
 i=i+1
print(l)