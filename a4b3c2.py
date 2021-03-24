s = 'a4b3c2'
output = ''
i=0
while i<len(s):
 if s[i].isalpha():
  ch = s[i]
  output = output+s[i]
 else:
  d=int(s[i])
  output=output+ch*(d-1)
 i=i+1
print(output)