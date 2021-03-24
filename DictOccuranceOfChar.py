word = input("Enter word")
d = {}
for ch in word:
 if ch in d:
  d[ch] = d.get(ch) + 1
 if ch not in d:
  d.setdefault(ch,1)
print(d)

def easymethod():
 for ch in word:
  d[ch] = d.get(ch,0)+1
 print(d)
