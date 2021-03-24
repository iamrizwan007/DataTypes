l = input("Enter elements of the list separated by ' ' (space) ").split()

def popwithoutindex():
 print("The last element of the list will be pop out: ",l.pop())
 print("list after popping out the element", l)
 con = input('''Do you want to continue 'Y' or 'N'
>> ''')
 if con == 'Y':
  if len(l)>0:
   popwithoutindex()
  else:
   print("Sorry, No element in the list to pop out, Thanks for using this software")
 if con == 'N':
  print("Thanks for using this software")

def popwithindex():
 print("The element at specified index will be pop out")
 index = int(input("Enter the index from {} to {} you want to remove element: ".format(0,len(l)-1)))
 print("element at provided index being pop out", l.pop(index))
 print("list after popping out the element", l)

op = int(input('''Please enter the option to chose how you want to remove the element:
1. Without Index
2. With Index
>> '''))
if op == 1:
 popwithoutindex()
if op == 2:
 popwithindex()
 