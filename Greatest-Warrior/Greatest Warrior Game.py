import random

#Introduction and Setup
print "Welcome to Greatest Warrior!"
inventory = {
	"Coins":0,
	"Equipped Weapon":[],
	"Equipped Armor":[],
	"Bag":[]
}

Defense = 0
Attack = 0
x = True

#Start Menu
while x:
	decision = raw_input("Stats, Inventory, Fight, or Shop?").lower()
	if Defense >= 500 & Attack >= 500:
		print "You are the greatest warrior!"
		x = False

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
			decision2 = raw_input("Equip Weapon or Equip Armor").lower()
			if decision2 == "equip weapon":
				print inventory["Bag"]
				decision3 = raw_input()

			if decision2 == "equip armor":
				print inventory["Bag"]
				decision4 = raw_input()

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
			x = False

		#Giant Enemy
		elif opponent > 48:
			print "A Giant has appeared!"
			if Defense > 100 & Attack > 100:
				print "You are the Greatest Warrior in all the Land!"
				x = False
			else:
				print "You were slain by the Giant!"
				x = False

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
		if shop1 == "buy":
			print shop
			shop2 = raw_input("Which item would you like to buy?")
		elif shop1 == "sell":
			print inventory["Bag"]
			shop3 = raw_input("Which item would you like to sell?")

	#Incase Input Isn't A Wanted Input
	else:
		inventory["Coins"] -= 5
		print "-5 Coins"

#End Of Game
print "Game End"
