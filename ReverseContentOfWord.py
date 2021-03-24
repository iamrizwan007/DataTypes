def CustomFN():
 s= input("enter the string: ")
 l = s.split()
 for word in l:
  print(str(word[::-1]), end=' ')

def UsingList():
 s= input("enter the string: ")
 l= s.split()
 l1= []
 for word in l:
  l1.append(word[::-1])
 print(' '.join(l1))
 
