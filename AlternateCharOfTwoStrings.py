s1 = 'ACEGIKMO'
s2= 'BDFHJLNP'
output= ''
i=0
while i<len(s1):
 output=output+s1[i]+s2[i]
 i=i+1
print(output)