a,b = input("Enter the element range you want to see the num divisible by 10").split()
l= [x for x in range(int(a),int(b)+1) if x%10==0]
print("The numbers divisible by 10 in range of 1 to 100 are:\n\n",l)