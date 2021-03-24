supermarket = {
		'store1':{
			'name':'Rizwan General Store',
			'items':[
					{'name':'soap','qty':20},
					{'name':'brush','qty':30},
					{'name':'pen','qty':40}
				]
			},
		'store2':{
			'name':'Rizwan Book Store',
			'items':[
					{'name':'python','qty':100},
					{'name':'Django','qty':200},
					{'name':'Java','qty':300},
				]
			}
		}

#To print the name of store 1

print('Name of store 1: ',supermarket.get('store1')['name'])
print('Name of store 1 with Alt approach: ',supermarket.get('store1').get('name'))

#To print names of all items present in store1:

for d in supermarket.get('store1').get('items'):
 print(d.get('name'),end='')
 print()

#To print Qty of Django

for d in supermarket.get('store2').get('items'):
 if d.get('name')=='Django':
  print("Django quantity is: ",d.get('qty'))


#print('Django qty is: ',supermarket.get('store2').get('items')[1].get('qty'))