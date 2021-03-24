s= 'abaaabcdcc'
d={}
s1 = ''
for ch in s:
 d[ch] = d.get(ch,0) + 1
for k,v in sorted(d.items()):
 print("{} is occuring {} times".format(k,v))
 s1=s1+str(k)+str(v)
print(s1)