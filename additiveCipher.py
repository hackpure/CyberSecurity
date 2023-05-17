#! usr/bin/env python 

'''
Problem Statement :
	Write A Python Script To Encrypt / Decrypt / Brute-Force The Key of Symmetric Key Algorithm : Additive Cipher
'''

import time

def bannerDisplay():
	print("\t    ___       __    ___ __  _               _______       __  ")
	print("\t   /   | ____/ /___/ (_) /_(_)   _____     / ____(_)___  / /_") 
	print("\t  / /| |/ __  / __  / / __/ / | / / _ \   / /   / / __ \/ __ \ ")
	print("\t / ___ / /_/ / /_/ / / /_/ /| |/ /  __/  / /___/ / /_/ / / / /")
	print("\t/_/  |_\__,_/\__,_/_/\__/_/ |___/\___/   \____/_/ .___/_/ /_/ ")
	print("\t                                               /_/            ")
	print("\n     Encrpyt / Decrypt / Brute-Force The Symmetric Key Cipher Algorithm \n")



def encryptionDataSet(charset : str) -> int:
	'This Function Takes Individual Character and Returns The Corresponding Integer Of The Data.'
	encryptDataDict = {
	'a' : 0,
	'b' : 1,
	'c' : 2,
	'd' : 3,
	'e' : 4,
	'f' : 5,
	'g' : 6,
	'h' : 7,
	'i' : 8,
	'j' : 9,
	'k' : 10,
	'l' : 11,
	'm' : 12,
	'n' : 13,
	'o' : 14,
	'p' : 15,
	'q' : 16,
	'r' : 17,
	's' : 18,
	't' : 19,
	'u' : 20,
	'v' : 21,
	'w' : 22,
	'x'	: 23,
	'y' : 24,
	'z' : 25,
	}
	return encryptDataDict[charset]


def decryptionDataSet(charset : int) -> str:
	'This Function Takes Individual Integer and Returns The Corresponding Character Of The Data.'
	decryptdataDict = {
	0 : 'A' ,
	1 : 'B',
	2 : 'C',
	3 : 'D',
	4 : 'E',
	5 : 'F',
	6 : 'G',
	7 : 'H',
	8 : 'I',
	9 : 'J',
	10 : 'K',
	11 : 'L',
	12 : 'M',
	13 : 'N',
	14 : 'O',
	15 : 'P',
	16 : 'Q',
	17 : 'R',
	18 : 'S',
	19 : 'T',
	20 : 'U',
	21 : 'V',
	22 : 'W',
	23 : 'X',
	24 : 'Y',
	25 : 'Z',
	}
	return decryptdataDict[charset]

def checkVerboseInput(userVar : str) -> str:
	setFlag = True
	while setFlag:
		if userVar == "yes" or userVar == "no":
			return True
			setFlag = False 
		else:
			return False 
			setFlag = False

def encryptData(plainText : str, encryptKey : int) -> str:
	'This Function Encrpyts The Given Plain Text.'
	cipherTextvalue = []
	cipherText = ''
	for i in plainText:
		cipherTextvalue.append((encryptionDataSet(i) + encryptKey) % 26)
	for i in cipherTextvalue:
		cipherText += decryptionDataSet(i)
	return cipherText


def decryptData(cipherText : str, decryptKey : int) -> str:
	'This Function Decrypts The Given Cipher Text.'
	plainTextvalue = []
	plainText = ''
	for i in cipherText.lower():
		dataSet = ((encryptionDataSet(i) - decryptKey) % 26)
		if dataSet > 0:
			negDataSet = ((encryptionDataSet(i) - decryptKey + 26) % 26)
			plainTextvalue.append(negDataSet)
		else:
			plainTextvalue.append(dataSet)
	for i in plainTextvalue:
		plainText += decryptionDataSet(i)
	return plainText


def bruteForceAttack(cipherText : str, plainText :  str) -> int:
	'This Function Attacks The Key Of The Additive Cipher by Comparing The Cipher Text and Plain Text.'
	flag = True
	key = 0
	verbose = input("Do You Want To Enable Verbose [yes/no] ----> ").lower()
	if verbose.isalpha() and verbose == "yes":
		while flag:
			print("Attacking The Key.... Hang On !")
			attackOnKey = decryptData(cipherText, key)
			print("[+] Attacking With Key", key, "Plain Text By Attacking Key", attackOnKey, "Original Plain Text ", plainText.lower())
			if attackOnKey == plainText:
				print("[+] Key Found ----> ", end = '')
				return key
				flag = False 
			else:
				print("[-] Key Failed ...\nRetrying ...")
				time.sleep(1)
				key = key + 1
	elif verbose.isalpha() and verbose == "no":
		while flag:
			attackOnKey = decryptData(cipherText, key)
			if attackOnKey == plainText:
				print("[+] Key Found ----> ", end = '')
				return key
				flag = False 
			else:
				key = key + 1

	else:
		print("[-] Invalid Input Detected !\n[+] Using Default Verbose Flag [no].")
		while flag:
			attackOnKey = decryptData(cipherText, key)
			if attackOnKey == plainText:
				print("[+] Key Found ----> ", end = '')
				return key
				flag = False 
			else:
				key = key + 1




def showMenu():
	bannerDisplay()
	time.sleep(1.8)
	print("1. Encrpyt ")
	print("2. Decrypt")
	print("3. Brute-Force")
	print("4. Exit \n")

	while True:
		try:
			userChoice = int(input("Enter The Task To Be Performed ----> "))
			if (userChoice < 1) or (userChoice > 4):
				print("[-] Error Incorrect Option.")
				continue
		except ValueError:
			print("[-] Error Incorrect Values Entered ...\n[-] Try Again !")
			continue

		if userChoice == 1:
			while True:
				plainText = input("Enter Your Plain Text ----> ")
				if plainText.isalpha() and plainText.islower():
					while True:
						try:
							encryptKey = int(input("Enter Your Encrpytion Key ----> "))
							if (encryptKey < 0) or (encryptKey > 25):
								print("[-] Please Enter A Encrpytion Key Between 0-25")
								continue
						except ValueError:
							print("[-] Error Invalid Values Detected.")
							continue
						else:
							cipherText = encryptData(plainText, encryptKey)
							print("Performing Some Dark Magic Behind .... ")
							time.sleep(3.5)
							print("Your Cipher Text ----> ", cipherText)
							break
				else:
					print("[-] Either Invalid Plain Text Or Plain Text In Upper Case.\n[-] Try Again.")
					continue
				break


		elif userChoice == 2:
			while True:
				cipherText = input("Enter Your Cipher Text ----> ")
				if cipherText.isalpha() and cipherText.isupper():	
					while True:
						try:
							decryptKey = int(input("Enter Your Decryption Key ----> "))
							if (decryptKey < 0) or (decryptKey > 25):
								print("[-] Please Enter A Encrpytion Key Between 0-25")
								continue
						except ValueError:
							print("[-] Error Invalid Values Detected.")
							continue
						else:
							plainText = decryptData(cipherText, decryptKey)
							print("Performing Some Dark Magic Behind ... ")
							time.sleep(3.5)
							print("Your Plain Text Is ----> ", plainText.lower())
							break

				else:
					print("[-] Either Invalid Cipher Text Or Cipher Text Value In Lower Case.\n[-] Try Again.")
					continue
				break
 

		elif userChoice == 3:
			while True:
				cipherText = input("Enter Your Cipher Text ----> ")
				if cipherText.isalpha() and cipherText.isupper():
					while True:		
						plainText = input("Enter Your Plain Text ----> ")
						if plainText.isalpha() and plainText.islower():
							keyFound = bruteForceAttack(cipherText, plainText.upper())
							time.sleep(1)
							print(keyFound)
							break
						else:
							print("[-] Either Invalid Plain Text Or Plain Text In Upper Case.\n[-] Try Again.")
							continue

				else:	
					print("[-] Either Invalid Cipher Text Or Cipher Text Value In Lower Case.\n[-] Try Again.")
					continue
				break

		elif userChoice == 4:
			print("Thanks For Using Additive Ciph")
			time.sleep(1.5)
			exit()

showMenu()