s= input("Enter the alphanumeric string to sort in Alpha-numeric sorting: ")
alphabets=''
digits=''
i=0
while i<len(s):
 if s[i].isalpha():
  alphabets=alphabets+s[i] 
 else:
  digits=digits+s[i]
 i=i+1
alphabets = ''.join(sorted(alphabets))
digits= ''.join(sorted(digits))
print(alphabets+digits)