vowels = ['a','e','i','o','u']
word = input("Enter the word in which you want to know the unique vowels")
newlist =[ch for ch in vowels if ch in word]
print("Available unique vowels are: {} and total unique vowels are {}".format(newlist,len(newlist)))