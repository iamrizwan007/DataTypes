s='aaaabbbccz'
count=1
output=''
char=s[0]
i=1
while i<len(s):
 if char==s[i]:
  prev= s[i]
  count=count+1
 else:
  output=output+prev+str(count)
  count=1
  char=s[i]
 if i==(len(s)-1):
  output = output+s[i]+str(count)
 i=i+1
print(output)
