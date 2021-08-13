
fruit={}
cart=[]
while True:
	print("Press 1 for add fruit details")
	print("Press 2 for delete fruit ")
	print("Press 3 for change name and rate of fruit")
	print("Press 4 for search  fruit details")
	print("Press 5 for display fruit details")
	print("Press 6 for Add to cart")
	print("Press 7 for Display cart")
	print("Press 8 for Quit")
	choice = int(input("Enter choice"))
	if choice == 1:
		fruit_id = int(input("\tEnter Fruit_id "))
		if fruit_id not in fruit.keys():
			fruit_name = input("\tEnter name ")
			rate= int(input("\tEnter rate "))
			imported_from = input("\tEnter the imported from ")
			import_date = input("\tEnter import_date ")
			buying_price = int(input("\tEnter buying_price "))
			temp ={
				"fruit_name":fruit_name,
				"rate":rate,
				"imported_from":imported_from,
				"import_date":import_date,
				"buying_price":buying_price,
			}
			fruit[fruit_id] = temp
		else:
			print("\tfruit id  already Taken")

	elif choice == 2:
			fid = input("\tEnter fruit id") 
			if fid not in fruit.keys():
				print("\tWrong fruit id")
			else:
				del fruit[fid]
	elif choice == 3:
		print(fruit)
		c = int(input('Enter fruit id : '))
		if c not in fruit.keys():
			print('Please provide right fruit id ')
		else:
			print('modify fruit data')
			fruit[c]['fruit_name'] = input('Enter new fruit name :')
			fruit[c]['rate'] =input('Enter new rate : ')
	elif choice == 4:
		name=input("enter the fruit name you want to search")
		rate=input("enter the fruit rate you want to search")
		found = False
		for i in fruit.values():
			if i["fruit_name"] == name and i["rate"] == rate:
				print("We found!!")
				found = True
				break
		if(found == False):
				print("Not Found!!!!")
	elif choice == 5: 
                print(fruit)
	elif choice == 6:
		for i in fruit.keys():
			print(f"press {i} for add to cart")
		cart.append(fruit[int(input('enter fruit id to add on cart : '))])
	elif choice == 8:
                break
	elif choice == 7:
		print(cart)
	else:
		print("Invalid choice")
