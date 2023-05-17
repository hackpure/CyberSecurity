#! usr/bin/env python 

'''
Problem Statement :
	Write A Python Script To Encrypt / Decrypt / Brute-Force The Key of Symmetric Key Algorithm : Multiplicative Cipher
'''

import time


def showBanner():
	print("\t    __  ___      ____  _    _______       __ ") 
	print("\t   /  |/  /_  __/ / /_(_)  / ____(_)___  / /_ ")
	print("\t  / /|_/ / / / / / __/ /  / /   / / __ \/ __ \ ")
	print("\t / /  / / /_/ / / /_/ /  / /___/ / /_/ / / / /")
	print("\t/_/  /_/\__,_/_/\__/_/   \____/_/ .___/_/ /_/ ")
	print("                                       /_/      ")
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
	denryptdataDict = {
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
	return denryptdataDict[charset]

def checkKey(encryptionKey : int, totalLength :int = 26) -> str:
	gcd = 0
	if encryptionKey < 26:
		small = encryptionKey
	else:
		small = totalLength
	for i in range(1, small + 1):
		if (encryptionKey % i == 0) and (totalLength % i == 0):
			gcd = i

	if gcd > 1:
		return False
	else:
		return True


def multiplicativeInverseOfKey(encryptKey : int) -> int:
	'This Function Calculates The Value Of Decryption Key'
	decryptionKey = 1
	flag = True
	while flag:
		if((encryptKey * decryptionKey) % 26 == 1):
			return decryptionKey
			flag = False
		else:
			decryptionKey += 1 


def encryptData(plainText : str, encryptKey : int) -> str:
	'This Function Encrpyts The Given Plain Text.'
	cipherTextValue = []
	cipherText = ""
	for i in plainText:
		cipherTextValue.append((encryptionDataSet(i) * encryptKey) % 26)
	for i in cipherTextValue:
		cipherText += decryptionDataSet(i) 
	return cipherText

def decryptData(cipherText : str, decryptKey : int) -> str:
	'This Function Decrypts The Given Cipher Text Using The Decryption Key'
	plainTextValue = []
	plainText = ""
	for i in cipherText.lower():
		plainTextValue.append((encryptionDataSet(i) * decryptKey) % 26)
	for i in plainTextValue:
		plainText += decryptionDataSet(i)
	return plainText

def bruteForceAttack(cipherText : str, plainText : str) -> int:
	'This Function Brute Forces The Key On The Data Provided.'
	encryptKey = 0 
	decryptKey = 0
	setFlag = True
	while setFlag:
		attackOnDecryptKey = decryptData(cipherText, decryptKey)
		if attackOnDecryptKey == plainText:
			setFlag	 = False
		else:
			decryptKey += 1
	setFlag = True
	if ask == "yes": 
		while setFlag:
			attackOnEncryptKey = encryptData(plainText.lower(), encryptKey)
			if attackOnEncryptKey == cipherText:
				setFlag = False
			else:
				encryptKey += 1
	return encryptKey, decryptKey



def showMenu():
	showBanner()
	time.sleep(0.6)
	print("1. Encrypt")
	print("2. Decrypt")
	print("3. Brute-Force")
	print("4. Exit\n")
	while True:
		try:
			userChoice = int(input("Enter The Task To Be Performed ----> "))
			if (userChoice < 1) or (userChoice > 4):
				print("[-] Error Incorrect Option.")
				time.sleep(0.5)
				continue
		except ValueError:
			print("[-] Error Incorrect Values Entered ... \n[-] Try Again !")
			time.sleep(0.5)
			continue
		

		if userChoice == 1:
			while True:
				plainText = input("Enter Your Plain Text ----> ")
				if plainText.isalpha() and plainText.islower():
					while True:
						try:
							encryptKey = int(input("Enter Your Encryption Key ----> "))
						except ValueError:
							print("[-] Invalid Values Detected.")
							time.sleep(0.5)
							continue
						else:
							print("[+] Validating Encryption Key .... ")
							time.sleep(0.5)
							validateEncryptionKey = checkKey(encryptKey)
							if validateEncryptionKey == True:
								print("[+] Key Validation Successful.")
								time.sleep(0.8)
								print("[+] Performing The Encryption.\n[+] Have Patient.")
								cipherText = encryptData(plainText, encryptKey)
								time.sleep(0.5)
								print("Your Cipher Text Is ----> ",cipherText)
								break
							elif validateEncryptionKey == False:
								print("[-] Error Invalid Key Because Key Isn't Co-Prime With The Encryption Data Set\n[-] Try Again.")
								time.sleep(0.5)
								continue
				else:
					print("[-] Either Invalid Plain Text Or Plain Text Value In Upper Case.\n[-] Try Again.")
					time.sleep(0.5)
					continue
				break


		elif userChoice == 2:
			while True:
				cipherText = input("Enter The Cipher Text ----> ")
				if cipherText.isalpha() and cipherText.isupper():
					while True:
						try:
							decryptionKey = int(input("Enter The Decryption Key ----> "))
						except ValueError:
							print("[-] Invalid Values Detected.")
							time.sleep(0.5)
							continue
						else:
							print("[+] Validating The Decryption Key .... ")
							time.sleep(0.5)
							validateDecryptionKey = checkKey(decryptionKey)
							if validateDecryptionKey == True:
								print("[+] Key Validation Successful.")
								time.sleep(0.8)
								print("[+] Perfroming The Decryption.\n[+] Have Patients.")
								plainText = decryptData(cipherText, decryptionKey)
								time.sleep(0.5)
								print("Your Plain Text Is ----> ", plainText.lower())
								break
							elif validateDecryptionKey == False:
								print("[-] Error Invalid Key Because Key Isn't Co-Prime With The Decryption Data Set\n[-] Try Again.")
								time.sleep(0.8)
								continue
				else:
					print("[-] Either Invalid Cipher Text Or Cipher Text Value In Lower Case.\n[-] Try Again.")
					time.sleep(0.8)
					continue
				break

		elif userChoice == 3:
			while True:
				cipherText = input("Enter Your Cipher Text ----> ")
				if cipherText.isalpha() and cipherText.isupper():
					while True:
						plainText = input("Enter Your Plain Text ----> ")
						if plainText.isalpha() and plainText.islower():
							usedEncryptKey, usedDecryptKey = bruteForceAttack(cipherText, plainText.upper())
							time.sleep(1.0)
							print("The Encryption Key Used Was : ", usedEncryptKey, " And The Decryption Key Used Will Be : ", usedDecryptKey)
							break
						else:
							print("[-] Either Invalid Plain Text Or Plain Text In Upper Case.\n[-] Try Again.")
							time.sleep(0.5)
							continue
				else:	
					print("[-] Either Invalid Cipher Text Or Cipher Text Value In Lower Case.\n[-] Try Again.")
					time.sleep(0.5)
					continue
				break


		elif userChoice == 4:
			print("[+] Thanks For Using Multi Ciph :)")
			time.sleep(0.9)
			exit()
showMenu()