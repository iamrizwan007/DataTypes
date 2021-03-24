s='a4k3b2'
output =''
for char in s:
 if char.isalpha():
  output=output+char
  unicode=ord(char)
 else:
  d=int(char)
  newchar=chr(unicode+d)
  output=output+newchar
print(output)