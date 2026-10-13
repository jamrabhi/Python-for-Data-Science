from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	"""Representing the King."""
	def __init__(self, first_name, is_alive=True):
		"""Initialize a King character."""
		super().__init__(first_name, is_alive)

	@property
	def eyes(self):
		return self.__dict__["eyes"]
		# We directly manipulate __dict__ to bypass the property
		# (avoiding RecursionError)
		# and to force the exact key name 'eyes' without an underscore
		# for the tester

	@eyes.setter
	def eyes(self, new_eyes):
		self.__dict__["eyes"] = new_eyes
	
	@property
	def hairs(self):
		return self.__dict__["hairs"]
	
	@hairs.setter
	def hairs(self, new_hairs):
		self.__dict__["hairs"] = new_hairs

	def get_eyes(self):
		return self.eyes

	def set_eyes(self, new_eyes):
		self.eyes = new_eyes

	def get_hairs(self):
		return self.hairs

	def set_hairs(self, new_hairs):
		self.hairs = new_hairs
