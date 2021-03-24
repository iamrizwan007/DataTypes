d = {
	'cars':('Innova','Honda','Maruti'),
	'mobiles':('Samsung','iPhone','Nokia')
	}
print(d['cars'][0])
print(d.get('cars')[1])
#To display all mobiles
for model in d.get('mobiles'):
 print(model, end=' ')