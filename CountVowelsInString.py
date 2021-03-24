s= input("Enter the string in which you want to count the number of vowels present: ")
v= 'aeiouAEIOU'
d={}
for ch in s:
 if ch in v:
  d[ch] = d.get(ch,0) + 1
for k,v in sorted(d.items()):
 print("{} vowel occuring {} times".format(k,v))