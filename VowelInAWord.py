vowelset = {'a','e','i','o','u'}
word = 'Rizwan'
s = set(word)
newset = s.intersection(vowelset)
print(newset)