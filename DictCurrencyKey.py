d = {'USD':'74.01 INR','AUD':'55.64 INR','FJD':'36.19 INR','EGP':'4.72 INR','EUR':'90.41 INR','JPY':'0.71 INR'}
ValCurr = input("Enter the Value '74.01 INR/55.64 INR/36.19 INR/4.72 INR/90.41 INR/0.71 INR' to know which currency has this value")
available = False
for k,v in d.items():
 if ValCurr==v:
  print(k)
  available = True
if available == False:
 print("No key associated with {} value".format(ValCurr))
