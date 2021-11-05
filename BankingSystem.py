userName = str(input('Enter your name: '))
userAge = int(input('Enter your age: '))
userGender = str(input('Enter your gender (Male | Female): '))
depositVal = int(input('Enter deposit amount: '))
withdrawVal = int(input('Enter withdraw amount: '))

class UserDetails():
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def account_info(self):
		print('\n Account Details \n')
		print('Name: ' + self.name)
		print('Age: ' + str(self.age))
		print('Gender: ' + self.gender)
  
class Actions(User):
	def __init__(self, name, age, gender):
		super().__init__(name, age, gender)
		self.balance = 0

	def deposit(self, amount):
		self.amount = amount
		self.balance = self.balance + self.amount
		print('Your current balance is: $' + str(self.balance))

	def withdrawal(self, amount):
		self.amount = amount
		if self.amount > self.balance:
			print('Insufficient balance')
		else:
			self.balance = self.balance - self.amount
			print('Balance after withdrawal: $' + str(self.balance))

	def display_balance(self):
		print('\nCurrent balance: $' + str(self.balance))
  
UserBank = Actions(userName, userAge, userGender)
UserInfo = UserDetails(userName, userAge, userGender)
UserInfo.account_info()
UserBank.deposit(depositVal)
UserBank.withdrawal(withdrawVal)
UserBank.display_balance()