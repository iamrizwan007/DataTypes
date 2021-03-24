a,b= input("Enter the number in range a to b separated by ' ' (space) for which you want to know square value\n>>").split()
l= [x*x for x in range(int(a),int(b)+1)]
print(l)