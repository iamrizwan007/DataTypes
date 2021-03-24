s = 'aaabchhhsajlkasn'
output=''
for char in s:
 if char not in output:
  output=output+char
print(output)