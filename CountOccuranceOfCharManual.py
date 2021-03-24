s1='aaaaabbbbcccdde'
s2=''
count=0
for ch in s1:
 if ch not in s2:
  s2=s2+ch
for ch in sorted(s2):
 for char in s1:
  if ch==char:
   count=count+1
 print("for string '{}', {} is occuring {} times".format(s1,ch,count))
 count=0