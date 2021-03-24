word = input("Enter the word to search occurance of vowel")
vowel = 'aeiou'
d = {}
for ch in word:
 if ch in vowel:
  d[ch] = d.get(ch,0) + 1
print(d)