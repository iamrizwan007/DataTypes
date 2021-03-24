s1="Hello"
s2="hi"
s3="1234"
i=j=k= 0
while i<len(s1):
 output=''
 if i<len(s1):
  output=output + s1[i]
  i+=1
 if j<len(s2):
  output=output + s2[j]
  j+=1
 if k<len(s3):
  output=output + s3[k]
  k+=1
 print(output)