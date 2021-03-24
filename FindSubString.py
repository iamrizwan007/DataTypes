s= input("Enter main string").strip() #strip() to remove spaces from beginning and end of the string
subs = input("Enter sub string").strip() #strip() to remove spaces from beginning and end of the string
i= s.find(subs) #0, if substring is ABC and main string is ABCABCABC
count=0
print("Total number of times substring is being repeated is :",s.count(subs)) 
if i==-1:
 print("{} not found in {}".format(subs,s))
else:
 while i!= -1:
  print("String found at index", i) 
  i = i+len(subs) #3
  i = s.find(subs,i)

  