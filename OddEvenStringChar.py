def SliceOP():
 s = "123456781"
 print("Character at odd index",s[0::2], end='')
 print("Character at even index",s[1::2], end='')

def WhileLoop():
 s = "123456"
 i=0
 print("Character present at even index:")
 while i<len(s):
  print(s[i])
  i=i+2
 i=1
 print("Character present at odd index:")
 while i<len(s):
  print(s[i])
  i=i+2
  
WhileLoop()