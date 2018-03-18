import random

#Title Screen
titleScreen = True
while titleScreen:
	print "G R E A T E S T   W A R R I O R"
	print "     Press Enter to Start"
	Start = raw_input()
	if Start == "":
		titleScreen = False
		
inventory = {
	"Coins":0,
	"Equipped Weapon":[],
	"Equipped Armor":[],
	"Bag":[]
}

shopItems = ["Wooden Shield: 15 Coins", "Bronze Shield: 20 Coins", "Iron Shield: 25 Coins", "Steel Shield: 35 Coins", "Boss Shield: 50 Coins", "Stick: 5 Coins", "Wooden Sword: 15 Coins", "Iron Sword: 30 Coins", "Steel Sword: 40 Coins", "Great Sword: 50 Coins"]

Defense = 0
Attack = 0
alive = True

#Start Menu
while alive:
	decision = raw_input("Stats, Inventory, Fight, or Shop?").lower()
	if Defense >= 500 & Attack >= 500:
		print "You are the greatest warrior!"
		alive = False

	#Stats Menu
	elif decision == "stats":
		stat1 = raw_input("Attack, Defense, or Items?").lower()
		if stat1 == "defense":
			print "Defense: " + str(Defense)
		elif stat1 == "attack":
			print "Attack: " + str(Attack)
		elif stat1 == "items":
			print inventory["Equipped Weapon"]
			print inventory["Equipped Armor"]
			print inventory["Bag"]
			stat2 = raw_input("Which item?")

	#Inventory Menu
	elif decision == "inventory":
		decision1 = raw_input("Coins, Equipped Weapon, Equipped Armor, Equip, or Bag?").lower()
		if decision1 == "equip":
			decision2 = raw_input("Equip Weapon or Equip Armor?").lower()
			if decision2 == "equip weapon":
				print inventory["Bag"]
				decision3 = raw_input()
				if (decision3 in inventory["Bag"]):
				  print "Noice"
				  if ("" in inventory["Equipped Weapon"]):
				    inventory["Equipped Weapon"].append(decision3)
				  
				
			if decision2 == "equip armor":
				print inventory["Bag"]
				decision4 = raw_input().lower()

		elif decision1 == "coins":
			print inventory["Coins"]
		elif decision1 == "equipped weapon":
			print inventory["Equipped Weapon"]
		elif decision1 == "equipped armor":
			print inventory["Equipped Armor"]
		elif decision1 == "bag":
			print inventory["Bag"]

	#Fight Menu
	elif decision == "fight":
		opponent = random.randint(1, 50)

		#Chuck Norris Enemy
		if opponent == 50:
			print "Chuck Norris has appeared!"
			print "You were slain by Chuck Norris"
			alive = False

		#Giant Enemy
		elif opponent > 48:
			print "A Giant has appeared!"
			if Defense > 100 & Attack > 100:
				print "You are the Greatest Warrior in all the Land!"
				alive = False
			else:
				print "You were slain by the Giant!"
				alive = False

		#Knight Enemy
		elif opponent > 44:
			print "A Knight has appeared!"
			if Defense > 55 & Attack > 65:
				Defense += 5
				print "+5 Defense"
				Attack += 6
				print "+6 Attack"
				addcoin1 = random.randint(35, 50)
				inventory["Coins"] += addcoin1
				print "+" + str(addcoin1) + " Coins"
				loot1 = random.randint(35, 50)
				if loot1 >= 46:
					inventory["Bag"].append("Steel Helmet")
					print "Special loot: +1 Steel Helmet" 
				elif loot1 >= 42:
					inventory["Bag"].append("Steel Longsword")
					print "Special loot: +1 Steel Longsword"
				elif loot1 >= 38:
					inventory["Bag"].append("Steel Chestplate")
					print "Special loot: +1 Steel Chestplate"
			else:
				Defense += 2
				print "+2 Defense"
				Attack += 1
				print "+1 Defense"
				inventory["Coins"] -= 4
				print "You lost 4 Coins"

		#Warrior Enemy
		elif opponent > 38:
			print "A Warrior has appeared!"
			if Defense > 65 & Attack > 55:
				Defense += 4
				print "+4 Defense"
				Attack += 5
				print "+5 Attack"
				addcoin2 = random.randint(25, 35)
				inventory["Coins"] += addcoin2
				print "+" + str(addcoin2) + " Coins"
				loot2 = random.randint(25, 35)
				if loot2 >= 32:
					inventory["Bag"].append("Iron Helmet")
					print "Special loot: +1 Iron Helmet"
				elif loot2 >= 29:
					inventory["Bag"].append("Black Blade")
					print "Special loot: +1 Black Blade"
				elif loot2 > 26:
					inventory["Bag"].append("Spear")
					print "Special loot: +1 Spear"
			else:
				Defense += 2
				print "+2 Defense"
				Attack += 1
				print "+1 Attack"
				inventory["Coins"] -= 3
				print "You lost 3 Coins"

		#Guard Enemy
		elif opponent > 30:
			print "A Guard has appeared!"
			if Defense >= 40 & Attack >= 40:
				Defense += 3
				print "+3 Defense"
				Attack += 4
				print "+4 Attack"
				addcoin3 = random.randint(15, 25)
				inventory["Coins"] += addcoin3
				print "+" + str(addcoin3) + " Coins"
				loot3 = random.randint(15, 25)
				if loot3 >= 22:
					inventory["Bag"].append("Wooden Shield")
					print "Special loot: +1 Wooden Shield"
				elif loot3 >= 19:
					inventory["Coins"] += 30
					print "Special loot: +30 Coins"
				elif loot3 > 16:
					inventory["Bag"].append("Battleworn Sword")
					print "Special loot: +1 Battleworn Sword"
			else:
				Defense += 2
				print "+2 Defense"
				Attack += 1
				print "+1 Attack"
				inventory["Coins"] -= 2
				print "You lost 2 Coins"

		#Citizen Enemy
		elif opponent > 20:
			print "A Citizen has appeared!"
			if Defense >= 25 & Attack >= 25:
				Defense += 2
				print "+2 Defense"
				Attack += 3
				print "+3 Attack"
				addcoin4 = random.randint(10, 20)
				inventory["Coins"] += addcoin4
				print "+" + str(addcoin4) + " Coins"
				loot4 = random.randint(10,20)
				if loot4 >= 17:
					inventory["Bag"].append("Helmet")
					print "Special loot: +1 Helmet"
				elif loot4 >= 14:
					inventory["Bag"].append("Stick")
					print "Special loot: +1 Stick"
				elif loot4 > 12:
					inventory["Coins"] += 25
					print "Special loot: +25 Coins"
			else:
				Defense += 2
				print "+2 Defense"
				Attack += 1
				print "+1 Attack"
				inventory["Coins"] -= 2
				print "You lost 2 Coins"

		#Wolf Enemy
		elif opponent > 10:
			print "A Wolf has appeared!"
			if Defense >= 15 & Attack >= 15:
				Defense += 1
				print "+1 Defense"
				Attack += 2
				print "+2 Attack"
				addcoin5 = random.randint(5, 15)
				inventory["Coins"] += addcoin5
				print "+" + str(addcoin5) + " Coins"
				loot5 = random.randint(5, 15)
				if loot5 >= 12:
					inventory["Bag"].append("Raw Wolf Meat")
					print "Special loot: +1 Raw Wolf Meat"
				elif loot5 >= 9:
					inventory["Bag"].append("Fur Coat")
					print "Special loot: +1 Fur Coat"
				elif loot5 > 6:
					inventory["Bag"].append("Sharp Fang")
					print "Special loot: +1 Sharp Fang"
			else:
				Defense += 2
				print "+2 Defense"
				Attack += 1
				print "+1 Attack"
				inventory["Coins"] -= 1
				print "You lost 1 Coin"

		#Giant Rat Enemy
		else:
			print "A Giant Rat has appeared!"
			if Defense >= 0 & Attack >= 0:
				Defense += 1
				print "+1 Defense"
				Attack += 1
				print "+1 Attack"
				addcoin6 = random.randint(3, 10)
				inventory["Coins"] += addcoin6
				print "+" + str(addcoin6) + " Coins"

	#Shop Menu
	elif decision == "shop":
		shop1 = raw_input("Buy or Sell?").lower()
		
		#Shop Buy Menu
		if shop1 == "buy":
			print shopItems
			shop2 = raw_input("Which item would you like to buy?").lower()
			if ((shop2 == "wooden shield") & (inventory["Coins"] >= 15)):
				inventory["Bag"].append("Wooden Shield")
				inventory["Coins"] -= 15
				print "-" + str(15) + " Coins"
			elif ((shop2 == "bronze shield") & (inventory["Coins"] >= 20)):
				inventory["Bag"].append("Bronze Shield")
				inventory["Coins"] -= 20
				print "-" + str(20) + " Coins"
			elif ((shop2 == "iron shield") & (inventory["Coins"] >= 25)):
				inventory["Bag"].append("Iron Shield")
				inventory["Coins"] -= 25
				print "-" + str(25) + " Coins"
			elif ((shop2 == "steel shield") & (inventory["Coins"] >= 35)):
				inventory["Bag"].append("Steel Shield")
				inventory["Coins"] -= 35
				print "-" + str(35) + " Coins"
			elif ((shop2 == "boss shield") & (inventory["Coins"] >= 50)):
				inventory["Bag"].append("Boss Shield")
				inventory["Coins"] -= 50
				print "-" + str(50) + " Coins"
			elif ((shop2 == "stick") & (inventory["Coins"] >= 5)):
				inventory["Bag"].append("Stick")
				inventory["Coins"] -= 5
				print "-" + str(addcoin6) + " Coins"
			elif ((shop2 == "wooden sword") & (inventory["Coins"] >= 15)):
				inventory["Bag"].append("Wooden Sword")
				inventory["Coins"] -= 15
				print "-" + str(15) + " Coins"
			elif ((shop2 == "iron sword") & (inventory["Coins"] >= 30)):
				inventory["Bag"].append("Iron Sword")
				inventory["Coins"] -= 30
				print "-" + str(30) + " Coins"
			elif ((shop2 == "steel sword") & (inventory["Coins"] >= 40)):
				inventory["Bag"].append("Steel Sword")
				inventory["Coins"] -= 40
				print "-" + str(40) + " Coins"
			elif ((shop2 == "great sword") & (inventory["Coins"] >= 50)):
				inventory["Bag"].append("Great Sword")
				inventory["Coins"] -= 50
				print "-" + str(50) + " Coins"
			else:
				print "You do not have enough Coins or the item isn't sold here"
				
		#Shop Sell Menu  
		elif shop1 == "sell":
			print inventory["Bag"]
			shop3 = raw_input("Which item would you like to sell?").lower()
			if ((shop3 == "wooden shield") & ("Wooden Shield" in inventory["Bag"])):
				inventory["Bag"].remove("Wooden Shield")
				inventory["Coins"] += 10
				print "+" + str(10) + " Coins"
			elif ((shop3 == "bronze shield") & ("Bronze Shield" in inventory["Bag"])):
				inventory["Bag"].remove("Bronze Shield")
				inventory["Coins"] += 15
				print "+" + str(15) + " Coins"
			elif ((shop3 == "iron shield") & ("Iron Shield" in inventory["Bag"])):
				inventory["Bag"].remove("Iron Shield")
				inventory["Coins"] += 20
				print "+" + str(20) + " Coins"
			elif ((shop3 == "steel shield") & ("Steel Shield" in inventory["Bag"])):
				inventory["Bag"].remove("Steel Shield")
				inventory["Coins"] += 25
				print "+" + str(25) + " Coins"
			elif ((shop3 == "boss shield") & ("Boss Shield" in inventory["Bag"])):
				inventory["Bag"].remove("Boss Shield")
				inventory["Coins"] += 30
				print "+" + str(30) + " Coins"
			elif ((shop3 == "stick") & ("Stick" in inventory["Bag"])):
				inventory["Bag"].remove("Stick")
				inventory["Coins"] += 5
				print "+" + str(5) + " Coins"
			elif ((shop3 == "wooden sword") & ("Wooden Sword" in inventory["Bag"])):
				inventory["Bag"].remove("Wooden Sword")
				inventory["Coins"] += 10
				print "+" + str(10) + " Coins"
			elif ((shop3 == "iron sword") & ("Iron Sword" in inventory["Bag"])):
				inventory["Bag"].remove("Iron Sword")
				inventory["Coins"] += 15
				print "+" + str(15) + " Coins"
			elif ((shop3 == "steel sword") & ("Steel Sword" in inventory["Bag"])):
				inventory["Bag"].remove("Steel Sword")
				inventory["Coins"] += 20
				print "+" + str(20) + " Coins"
			elif ((shop3 == "sharp fang") & ("Sharp Fang" in inventory["Bag"])):
				inventory["Bag"].remove("Sharp Fang")
				inventory["Coins"] += 4
				print "+" + str(4) + " Coins"
			elif ((shop3 == "fur coat") & ("Fur Coat" in inventory["Bag"])):
				inventory["Bag"].remove("Fur Coat")
				inventory["Coins"] += 8
				print "+" + str(8) + " Coins"
			elif ((shop3 == "raw wolf meat") & ("Raw Wolf Meat" in inventory["Bag"])):
				inventory["Bag"].remove("Raw Wolf Meat")
				inventory["Coins"] += 2
				print "+" + str(2) + " Coins"
			elif ((shop3 == "helmet") & ("Helmet" in inventory["Bag"])):
				inventory["Bag"].remove("Helmet")
				inventory["Coins"] += 10
				print "+" + str(10) + " Coins"
			elif ((shop3 == "battleworn sword") & ("Battleworn Sword" in inventory["Bag"])):
				inventory["Bag"].remove("Battleworn Sword")
				inventory["Coins"] += 10
				print "+" + str(10) + " Coins"
			elif ((shop3 == "spear") & ("Spear" in inventory["Bag"])):
				inventory["Bag"].remove("Spear")
				inventory["Coins"] += 15
				print "+" + str(15) + " Coins"
			elif ((shop3 == "black blade") & ("Black Blade" in inventory["Bag"])):
				inventory["Bag"].remove("Black Blade")
				inventory["Coins"] += 15
				print "+" + str(15) + " Coins"
			elif ((shop3 == "iron helmet") & ("Iron Helmet" in inventory["Bag"])):
				inventory["Bag"].remove("Iron Helmet")
				inventory["Coins"] += 15
				print "+" + str(15) + " Coins"
			elif ((shop3 == "steel helmet") & ("Steel Helmet" in inventory["Bag"])):
				inventory["Bag"].remove("Steel Helmet")
				inventory["Coins"] += 20
				print "+" + str(20) + " Coins"
			elif ((shop3 == "steel longsword") & ("Steel Longsword" in inventory["Bag"])):
				inventory["Bag"].remove("Steel Longsword")
				inventory["Coins"] += 20
				print "+" + str(20) + " Coins"
			elif ((shop3 == "steel chestplate") & ("Steel Chestplate" in inventory["Bag"])):
				inventory["Bag"].remove("Steel Chestplate")
				inventory["Coins"] += 20
				print "+" + str(20) + " Coins"
			else:
			  print "I don't accept that here!"

	#Incase Input Isn't A Wanted Input
	else:
		inventory["Coins"] -= 5
		print "-5 Coins"

#End Of Game
print "Game End"