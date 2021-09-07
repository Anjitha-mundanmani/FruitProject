from fruit_store import fruits

class Fruits:
	def __init__(self,fid,name,rate,imp_fr,imp_date,buy_rs):
		self.Fruit_Id = fid
		self.Name = name
		self.Rate = rate
		self.Imported_From = imp_fr
		self.Imported_Date = imp_date
		self.Buying_Price = buy_rs

def add_fruits():
	fid = int(input("\tEnter the Fruit Id : "))
	name = input("\tEnter the name of Fruit : ")
	rate = int(input("\tEnter the rate of Fruit : "))
	imp_fr = input("\tEnter the place imported from : ")
	imp_date = input("\tEnter the imported date : ")
	buy_rs = int(input("\tEnter the buying Price : "))
	if fid not in fruits.keys():
		fruits[fid] = Fruits(fid,name,rate,imp_fr,imp_date,buy_rs)

	else:
		print("\tFruit Id id is already present")

def delete_fruit():
	fid = int(input("\tEnter the Fruit id : "))
	n = input("\tEnter the name to delete : ")
	if (fid in fruits.keys()):
		if fruits[fid].Name == n:
			del fruits[fid]
			print("\tFruit deleted Successfully")
		else:
			print("\tFruit is not found")
	else:
		print("\tFruit id is incorrect")

def search_fruit():
	n = input("\tEnter the name to search : ")
	r = int(input("\tEnter the rate to search : "))
	f = False
	for i in fruits.values():
		if i.Name == n and i.Rate == r:
			print(f"\t{i.Name} is found")
			f = True
			break
	if f == False:
		print("\tNot Found")

def change_menu():
	print("\tenter 1 for Change Fruit Name")
	print("\tenter 2 for Change Fruit Rate")
	print("\tenter 3 for exit")

def change_fruit():
	while True:
		change_menu()
		ch = int(input("\tEnter the choice : "))
		if ch == 3:
			break
		fid = int(input("\tEnter the Fruit Id : "))
		if fid in fruits.keys():
			if ch == 1:
				fruits[fid].Name = input("\tEnter the new Name : ")
				print("\tFruit Name Changed")
			elif ch == 2:
				fruits[fid].Rate = int(input("\tEnter the new Rate : "))
				print("\tFruit Rate Changed")
			else:
				print("\tFruit Not Found")


def display_fruits():
	for i, j in fruits.items():
		print(f"\t{i} => {j.Name} | {j.Rate} | {j.Imported_From} | {j.Imported_Date} | {j.Buying_Price}")
