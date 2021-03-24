n = int(input("Enter the number of students whose marks to be read"))
d = {}
i= 1
while i<n+1:
 name = input("name of student {}: ".format(i))
 marks = input("Enter the marks of {}: ".format(name))
 d[name]=marks
 i=i+1
print('*' * 30)
print("Name",'\t\t',"Marks")
print('*' * 30)
for key,value in d.items():
 print(key,'\t\t',value)