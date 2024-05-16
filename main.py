

accountBegum = {
	'name' : 'Begum Oral',
	'accountNo' : '111222333', 
	'balance' : 3000,
	'overdraft' : 2000
}

accountEsin = {
	'name' : 'Esin Cavusoglu',
	'accountNo' : '111222334',
	'balance' : 2000,
	'overdraft' : 1000
}

def withdraw(account, amount):
	print(f"Merhaba {account['name']}")

	if (account['balance'] >= amount):
		print("You can withdraw your money.")

		while True:

			yesNo = int(input("Press 1 to proceed with withdrawal, press 2 to quit. "))
		
			if (yesNo == 1):
				account['balance'] -= amount
				print(f"Withdrawal successful, you now have {account['balance']} left in your account.")
				break
			elif (yesNo == 2):
				print("Quitting the withdrawal process...")
				print(" Program is now ending...")
				break
	else:
		total = account['balance'] + account['overdraft']

		if (total >= amount):
	
			while True:

				yesNo = int(input("Insufficient balance in the main account. If you wish to use your overdraft account: Press 1 to proceed with withdrawal, press 2 to quit. "))
		
				if (yesNo == 1):
					account['overdraft'] = total - account['balance']
					account['balance'] = 0
					print(f"Withdrawal successful, you now have {account['balance']} left in your main account and {account['overdraft']} left in your overdraft account.")
					break
				elif (yesNo == 2):
					print("Quitting the withdrawal process...")
					print(" Program is now ending...")
					break

withdraw(accountBegum, 5000)