print()

print('''**********************************************************************************************************
                 Program to reverse a string using 3 different methods, Designed by Rizwan                
**********************************************************************************************************''')

s = input("enter the string you want to reverse: ")

def UsingSliceOP():	#Method 1
 reverse = s[::-1]	#As step value is -1, it will consider in backward direction considering all the string
 print("The reversed string is :",reverse)

def UsingReverseFN():	#Method 2
 x = reversed(s)
 print("The reversed string is:",''.join(x))
#Alternate:
#for ch in x:
#  print(ch, end='')

def UsingWhileLoop():	#Method 3
 rstring = ''
 i=0 
 while i<len(s):
  rstring = rstring + s[-(i+1)]
  i+=1
 print(rstring)

print()

x =int(input('''Please select the method(1, 2, or 3) to reverse the string
1. UsingSliceOP()
2. UsingReverseFN()
3. UsingWhileLoop()
enter (1,2, or 3) : '''))

print()

if x==1:
 UsingSliceOP()
if x==2:
 UsingReverseFN()
if x==3:
 UsingWhileLoop()
if x!=1 and x!=2 and x!=3:
 print("Please enter valid input")