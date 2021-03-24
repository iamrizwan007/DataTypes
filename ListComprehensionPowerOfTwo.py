a,b = input("Enter the range of element separated by ' ' (space) for which you seek value to the power of 2\n>>").split()
l = [2**x for x in range(int(a),int(b)+1)]
print(l)