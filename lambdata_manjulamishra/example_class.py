"""
Bank Example: a simple example banking
https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
"""

class Customer(object):
	"""
	A customer of ABC Bank with a checking account. Customers have the following properties:

	Attributes:
	 	name: A string representing the customer's name. 
	 	balance: A flaot tracking the current balance of the customer's account.
	"""

	def __init__(self, name, balance=0.0):
		"""retunr a Customer object whose name is *name* and starting balance is *balance*
		"""
		self.name = name
		self.balance = balance

	def withdraw(self, amount):
		"""Return the balance remaining after withdrawing *amount* dollars."""
		if amount > self.balance:
			raise RuntimeError('Amount greater than available balance')
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
	"""Return the balance remaining after depositing *amount* dollars"""
		self.balance += amount
		return self.balance


