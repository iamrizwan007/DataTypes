l1 = [10,10,20,30,40]
l2=[] + l1
print("List contains elements",l1)
x = int(input("Enter the element to be removed: "))
while x in l1:
 if x in l1:
  l1.remove(x)
 #print(x,"removed","New list: ", l1)
if l1==l2:
 print("Entered element not in the list")
else:
 print("Element removed",l1)
