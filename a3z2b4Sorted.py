s=input("Enter characted of string followed by numeric digit for char repetition and to view sorted result:")
output=''
i=0
while i<len(s):
 if s[i].isalpha():
  ch=s[i]
  output= output+s[i]
 else:
  d= int(s[i])
  output= output+ch*(d-1)
 i=i+1
print(''.join(sorted(output)))