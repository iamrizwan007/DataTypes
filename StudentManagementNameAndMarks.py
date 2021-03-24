d ={}
def inputrecord():
 n = int(input("How many students you want to add"))
 for x in range(1,n+1):
  sname = input("Please enter {} student name ".format(x))
  marks = input("Please enter {} student marks ".format(x))
  d[sname] = marks
 print("Record has been updated and the updated list is:")
 for k,v in d.items():
  print("{}      {}".format(k,v))
 con = input("Do you want to continue? Y/N")
 if con.lower() =='y':
  admin = int(input('''Which task you want to perform: 
1.Enter a new record
2.Search the marks of student
>>'''))
  if admin==1:
   inputrecord()
  if admin==2:
   markssearch()
 if con.lower() =='n':
  print("Thanks for using the application")
def markssearch():
 while True:
  sname = input("Please enter student name to search the marks")
  retrieve = d.get(sname,-1)
  if retrieve == -1:
   print("Not Found")
  else:
   print("Marks: ",retrieve)
   break
 print("Thanks for using the application")

inputrecord()