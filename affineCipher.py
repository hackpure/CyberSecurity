#! usr/bin/bash python

'''

Problem Statement : Design and Implement Affine Cipher

'''

import time

def showBanner():
	pass

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

def affineEncryption(plainText : str, multiEncryptKey : int, additiveEncryptKey : int) -> str:
	cipherTextValue = []
	cipherText = ""
	for i in plainText:
		cipherTextValue.append(((encryptionDataSet(i) * multiEncryptKey) + additiveEncryptKey) % 26)
	for i in cipherTextValue:
		cipherText += decryptionDataSet(i)
	return cipherText

def affineDecryption(cipherText : str, multiDecryptKey : int, additiveDecryptKey : int) -> int:
	plainTextValue = []
	plainText = ""
	for i in cipherText.lower():
		dataSet = (((encryptionDataSet(i) - additiveDecryptKey) * multiDecryptKey) % 26)
		if dataSet > 0:
			negDataSet = (((encryptionDataSet(i) - additiveDecryptKey + 26) * multiDecryptKey) % 26)
			plainTextValue.append(negDataSet)
		else:
			plainText.append(dataSet)
	for i in plainTextValue:
		plainText += decryptionDataSet(i)
	return plainText

def inverseKey(encryptKey : int) -> int:
	decryptionKey = 1
	flag = True
	while flag:
		if((encryptKey * decryptionKey) % 26 == 1):
			return decryptionKey
			flag = False
		else:
			decryptionKey += 1


def bruteForceAffine(plainText : str, cipherText : str) -> int:
	multiEncryptKey = 0
	additiveEncryptKey = 0
	for addKey in range(0, 25):
		for multiKey in range(0, 25):
			attackOnAffineEncrpytKey = affineEncryption(plainText, multiKey, addKey)
			if attackOnAffineEncrpytKey == cipherText:
				multiEncryptKey = multiKey
				additiveEncryptKey = addKey

	attackOnAffineDecryptionKey = inverseKey(multiEncryptKey)

	return multiEncryptKey, additiveEncryptKey, attackOnAffineDecryptionKey

def validateMultiplicativeKey(encryptionKey : int, totalLength : int = 26) -> bool:
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


def mainMenu():
	print("1. Encrypt")
	print("2. Decrypt")
	print("3. Brute-Force")
	print("4. Exit")


	while True:
		try:
			userChoice = int(input("Enter Your Task To Be Performed : "))
			if (userChoice < 1 ) or (userChoice > 4):
				print("[-] Invalid Option Opted... \n[-] Try Again.")
				continue
		except ValueError:
			print("[-] Invalid Values Detected... \n[-] Try Again.")
			continue

		if userChoice == 1:
			while True:
				plainText = input("Enter Your Plain Text : ")
				if plainText.isalpha() and plainText.islower():
					while True:
						try:
							multiEncryptKey = int(input("Enter Your First Encryption Key : "))
						except ValueError:
							print("[-] Invalid Values Detected... \n[-] Try Again.")
							continue
						else:
							print("[+] Validating First Encryption Key.... ")
							time.sleep(0.8)
							validationOfKey = validateMultiplicativeKey(multiEncryptKey)
							if validationOfKey == True:
								print("[+] Key Validation SuccessFul...")
								time.sleep(0.5)
								while True:
									try:
										additiveEncryptKey = int(input("Enter Your Second Encryption Key : "))
									except ValueError:
										print("[-] Invalid Values Detected... \n[-] Try Again.")
										continue
									else:
										encryptedMessage = affineEncryption(plainText, multiEncryptKey, additiveEncryptKey)
										print("Your Cipher Text Is : ", encryptedMessage)
										break
							elif validationOfKey == False:
								print("[-] Error Invalid Key Because Key Isn't Co-Prime With The Encryption Data Set\n[-] Try Again.")
								continue
						break
				else:
					print("[-] Invalid Message... \n[-] Try Again.")
					continue
				break
		
		elif userChoice == 2:
			while True:
				cipherText = input("Enter Your Cipher Text : ")
				if cipherText.isalpha() and cipherText.isupper():
					while True:
						try:
							multiDecryptKey = int(input("Enter Your First Decryption Key : "))
						except ValueError:
							print("[-] Invalid Values Detected... \n[-] Try Again.")
							continue
						else:
							print("[+] Validating First Decryption Key.... ")
							time.sleep(0.5)
							validationOfKey = validateMultiplicativeKey(multiDecryptKey)
							if validationOfKey == True:
								print("[+] Validation SuccessFul... ")
								while True:
									try:			
										additiveDecryptKey = int(input("Enter Your Second Decryption Key : "))
									except ValueError:
										print("[-] Invalid Values Detected... \n[-] Try Again.")
										continue
									else:
										decryptedMessage = affineDecryption(cipherText, multiDecryptKey, additiveDecryptKey)
										print("Your Plain Text Is : ", decryptedMessage.lower())
										break
							elif validationOfKey ==  False:
								print("[-] Error Invalid Key Because Key Isn't Co-Prime With The Encryption Data Set\n[-] Try Again.")
								continue
						break
				else:
					print("[-] Invalid Message... \n[-] Try Again.")
					continue
				break

		elif userChoice == 3:
			while True:
				plainText = input("Enter Your Plain Text : ")
				if plainText.isalpha() and plainText.islower():
					while True:
						cipherText = input("Enter Your Cipher Text : ")
						if cipherText.isalpha() and cipherText.isupper():
							crackedMultiEncryptionKey, crackedAddEncryptionKey, crackedMultiDecryptionKey = bruteForceAffine(plainText, cipherText)
							print("Key Pairs Used For Encryptions Are :", crackedMultiEncryptionKey, crackedAddEncryptionKey, "\nKey Pair That Will Be Used For Decryption Are : ", crackedMultiDecryptionKey, crackedAddEncryptionKey)
							break
						else:
							print("[-] Invalid Message... \n[-] Try Again.")
							continue
				else:
					print("[-] Invalid Message... \n[-] Try Again.")
					continue
				break

		elif userChoice == 4:
			print("Thanks For Using Affine Ciph ;)")
			time.sleep(0.8)
			exit()
mainMenu()