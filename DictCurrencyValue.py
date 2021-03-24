d = {'USD':'74.01 INR','AUD':'55.64 INR','FJD':'36.19 INR','EGP':'4.72 INR','EUR':'90.41 INR','JPY':'0.71 INR'}
currency = input("Enter the currency 'UDS/AUD/FJD/EGP/EUR/JPY' for which you want to know the value in INR")
if currency in d:
 print(d.get(currency))
else:
 print("not supported")