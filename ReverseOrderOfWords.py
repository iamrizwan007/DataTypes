def CustomFN():
 s = input("Enter the string: ")
 i=0
 while i!=-1:
  i = s.rfind(' ') #-1
  print(s[i+1:len(s)], end=' ')
  s = s[0:i:1]

def UsingList():
 s = input("Enter the string: ")
 l = s.split()
 print(' '.join(l[::-1]))

x =int(input('''Please select the method(1, 2, or 3) to reverse the string
1. CustomFN()
2. UsingList()
enter (1,or 2) : '''))

print()

if x==1:
 CustomFN()
if x==2:
 UsingList()
if x!=1 and x!=2:
 print("Please enter valid input")