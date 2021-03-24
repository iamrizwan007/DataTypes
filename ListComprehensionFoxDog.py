s = 'the quick brown fox jumps over the lazy dog'
word = s.split()
newlist = [[x.upper(),len(x)] for x in word]
print(newlist)