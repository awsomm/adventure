import random

townpreNames = ["New", "Hamp", "Shef", "Eman", "Omen", "Quish", "Vall", "Loren", "Eren"]
townAftNames = ["burg", "topia", "ia", "bury", "town", "ville", "ford", "dal", "ial", "fort"]
name = input("What is your name young traveler? \n")
playerHpMax = 5
playerHp = 5
playerDmg = 1
Coins = 10
resistance = 1
critChance = 0
inv = [00]

startTown = townpreNames[random.randint(0, 8)] + townAftNames[random.randint(0, 9)]
print("Welcome to the village of " + startTown + ", " +  name + "!")

 
SC1 = input(name + "! There are bandits attacking " + startTown + "! What should we do? \nA) Get everyone inside \nB) Prepare to fight! \n(Input your answer as one capital letter) \n")
if SC1 == "A":
	Coins = Coins - 2
	print ("Everyone is safe inside but the bandits took 2 gold from the village storage.")
	Weapon = input("There is one bandit left, choose a weapon to take him out.\nA) Sword \nB) Bow \nC) Wand \n")
	if Weapon == "A":
		Class = "Warrior"
		Attack = "Slash with your Sword"
		weaponList = ["Longsword", "Sheild", "Chainmail Armor"]
		weaponPrice = [5, 5, 7]
	if Weapon == "B":
		Class = "Ranger"
		Attack = "Shoot with your Bow"
		weaponList = ["Crossbow", "Amulet of Critical Strike", "Smoke Bomb"]
		weaponPrice = [5, 5, 7]
	if Weapon == "C":
		Class = "Mage"
		Attack = "Cast a spell with your Wand"
		weaponList = ["Staff", "Healing Spell", "Spell of Freezing"]
		weaponPrice = [5, 6, 9]
if SC1 == "B":
	Weapon = input("Grab a weapon, and go fight! \nA) Sword \nB) Bow \nC) Wand \n")
	if Weapon == "A":
		Class = "Warrior"
		Attack = "Slash with your Sword"
		weaponList = ["Longsword", "Shield", "Chainmail Armor"]
		weaponPrice = [5, 5, 7]
	if Weapon == "B":
		Class = "Ranger"
		Attack = "Shoot with your Bow"
		weaponList = ["Crossbow", "Amulet of Critical Strike", "Smoke Bomb"]
		weaponPrice = [5, 5, 7]
	if Weapon == "C":
		Class = "Mage"
		Attack = "Cast a spell with your Wand"
		weaponList = ["Staff", "Healing Spell", "Spell of Freezing"]
		weaponPrice = [5, 6, 9]
print("Good choice young " + Class + "! " + name + ", attack the Bandit!")

def battle (Hp,Dmg,Cc, Enemy):
	global playerDmg
	global playerHp
	global playerHpMax
	global critChance
	
	Acc = 0
	enemyHp = Hp
	enemyDmg = Dmg
	ogDmg = playerDmg
	while enemyHp > 0:
		Acc = 0
		enemyDmg = Dmg
		enemyAct = random.randint(1,2)
		enemyCrit = random.randint(Cc, 99)
		if Class == "Mage" and len(inv) == 3:
			 Action = input("\nA) " + Attack + " (Deal damage to the " + Enemy + ")\nB) Defend (Protect yourself, making enemies deal less damage)\nC) Freeze spell \nD) Heal Spell\n")

			 
		elif Class == "Mage" and 'FzSpell' in inv and len(inv) == 2:
			Action = input("\nA) " + Attack + " (Deal damage to the " + Enemy + ")\nB) Defend (Protect yourself, making enemies deal less damage)\nC) Freeze spell \n")
		elif Class == "Mage" and 'HpSpell' in inv and len(inv) == 2:
			Action = input("\nA) " + Attack + " (Deal damage to the " + Enemy + ")\nB) Defend (Protect yourself, making enemies deal less damage)\nC) Heal Spell\n")
		elif Class == "Ranger" and 'smokeBomb' in inv and len(inv) == 2:
			Action = input("\nA) " + Attack + " (Deal damage to the " + Enemy + ")\nB) Defend (Protect yourself, making enemies deal less damage)\nC) Smoke Bomb\n")
		else :
			Action = input("\nA) " + Attack + " (Deal damage to the " + Enemy + ")\nB) Defend (Protect yourself, making enemies deal less damage)\n")	
		
		if Action == "A":
			enemyHp = enemyHp - playerDmg
			if random.randint(critChance, 99) == 99:
				print ("\nCRITICAL HIT!")
				enemyHp = enemyHp - playerDmg
				playerDmg = ogDmg
			if enemyHp < 0:
				enemyHp = 0
			print("\nThe " + Enemy + " has " + str(enemyHp) + " health left!")
		if Action == "B":
			enemyDmg = enemyDmg / 2
		if Action == "C":
			if Class == "Mage" and 'HpSpell' in inv and len(inv) == 2:
				playerHp = playerHp + 1
				print("\nYou healed yourself for 1 Hp! Your health is now: " + str(playerHp) + "!")
			if Class == "Mage" and 'FzSpell' in inv and len(inv) == 2:
				enemyAct = 3
				print("\nThe " + Enemy + " is frozen!")
			if Class == "Ranger" and 'smokeBomb' in inv and len(inv) == 2:
				print("\nThe " + Enemy + " is now confused")
				Acc = 1
				
		if enemyHp <= 0 :
			print("\nThe " + Enemy + " has fallen")
			playerDmg = ogDmg
			enemyDmg = Dmg
			break 
		
		playerDmg = ogDmg
		
		if enemyAct == 1:
			if random.randint(1,3) != Acc:
				playerHp = playerHp - enemyDmg
				print("\nThe " + Enemy + " attacks you! you are now at: " + str(playerHp) + " health")
			else:
				print("\nThe " + Enemy + " swung missed you because of the smoke!")
		if enemyAct == 2:
			print("\nThe " + Enemy + " raises his stance ready for your next move.")
			playerDmg = playerDmg / 2
		if playerHp <= 0:
			print("\nYou have fallen to the hands of your " + Enemy + ".\nGAME OVER...")
			enemyDmg = Dmg
			exit()

battle(3, 1, 0, "Bandit")

print("\nThank you for saving " + str (startTown) + ", " + name + "! Please, take this " + str (Coins) + " coins for our gratitude.")
	
def shop():
	global playerHpMax
	global playerDmg
	global critChance
	global Coins
	global resistance
	
	SC2 = input("\nWould you like to purchase anything from the shop?\nA) Yes\nB) No\n")
	optionA = random.randint(0,2)
	optionB = random.randint(0,2)
	while optionA == optionB:
		optionA = random.randint(0,2)
	if SC2 == "A":
		buy = input ("\nBlacksmith: Hello " + str(name) + ", you may buy " + str(weaponList[optionA]) + " for " + str(weaponPrice[optionA]) + " or " + str(weaponList[optionB]) + " for " + str(weaponPrice[optionB]) + "\n" + "A) For option 1 \nB) For option 2 \nC) For nothing\n") 
		if buy == "A":
			print("Thanks for the purchase of " + weaponList[optionA] + "!\n")
			if optionA == 0:
				playerDmg = playerDmg + 0.5
				print("Your damage is now greater.")
				Coins -= 5
			if str(optionA) == "1" and Class == "Warrior":
				resistance = 0.9
				print("You take less damage from enemy attacks now.")
				Coins -= 5
			if str(optionA) == "1" and Class == "Ranger" :
				critChance = 10
				print("Your chances of critically damaging your enemy is now higher!")
				Coins -= 5
			if str(optionA) == "1" and Class == "Mage" :
				inv.append("HpSpell")
				print("You can now cast a healing spell in battle!")
				Coins -= 6
			if str(optionA) == "2" and Class == "Warrior" :
				playerHpMax = playerHpMax + 0.5
				print("You are now more defended in battle!")
				Coins -= 7
			if str(optionA) == "2" and Class == "Ranger" :
				inv.append("smokeBomb")
				print("Confuse your enemies with this wall of smoke")
				Coins -= 7
			if str(optionA) == "2" and Class == "Mage" and Coins >= 9:
				if Coins < 9:
					print("You don't have enough money for that!")
				else 
					Coins -= 9
					inv.append("FzSpell")
					print("You can now cast a freezing spell in battle!")
		if buy == "B":
			print("Thanks for the purchase of " + weaponList[optionB] + "!\n")
			if optionB == 0:
				playerDmg = playerDmg + 0.5
				print("Your damage is now greater.")
				Coins -= 5
			if str(optionB) == "1" and Class == "Warrior" :
				resistance = 0.9
				print("You take less damage from enemy attacks now.")
				Coins -= 5
			if str(optionB) == "1" and Class == "Ranger" :
				critChance = 10
				print("Your chances of critically damaging your enemy is now higher!")
				Coins -= 5
			if str(optionB) == "1" and Class == "Mage" :
				inv.append("HpSpell")
				print("You can now cast a healing spell in battle!")
				Coins -= 6
			if str(optionB) == "2" and Class == "Warrior" :
				playerHpMax = playerHpMax + 0.5
				print("You are now more defended in battle!")
				Coins -= 7
			if str(optionB) == "2" and Class == "Ranger" :
				inv.append("smokeBomb")
				print("Confuse your enemies with this wall of smoke")
				Coins -= 7
			if str(optionB) == "2" and Class == "Mage" :
				inv.append("FzSpell")
				print("You can now cast a freezing spell in battle!")
				Coins -= 9

	print ("Blacksmith: Bye " + name + ".")
	
shop()

print ("Now this day is over, you may rest and restore your health.")
playerHp = playerHpMax

print("\nDAY 2\n")
##DAY2##

print("Ah, good morning " + name + ", I'm glad you slept well.\nThere is a bandit camp on the outskirts of the forest, they have been killing civillians and harrassing the town. You should go there and attack it!")
berry = input("\nYou are walking through the forest, and you come across a berry bush. Do you eat a berry?\nA) Yes\nB) No\n")
if berry == "A":
	Poison = random.randint(0,1)
	if Poison == 1:
		print("You ate a berry, and it made you take damage")
		playerHp = playerHp - 0.5
	if Poison == 0:
		print("You ate a berry, and it heals you!")
		playerHp = playerHp + 0.5
print("\nYou continue walking along the path toward the bandit camp, when suddenly, you are ambushed by a Bandit!")
battle(3, 1, 0, "Bandit")
print("\nAs you arrive at the bandit camp, you jump into the fray and attack the last Bandit!")
battle(3, 1, 0, "Bandit")
print("\nAs the bandit falls, a map slips out of his pocket, along with 5 coins."
