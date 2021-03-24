s1 = 'aaabbbcccdefffffffffffff'
s2=''
for char in s1:
 if char not in s2:
  s2=s2+char
for char in s2:
 print("number of {} in s1 is {}".format(char,s1.count(char)))