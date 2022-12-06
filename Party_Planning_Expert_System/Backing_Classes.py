from experta import *


class Food(Fact):
	pass


class Menu(Fact):
	pass


class Drinks(Fact):
	pass


class Alcoholic(Fact):
	pass


class MusicPlaylist(Fact):
	pass


class Themes(Fact):
	pass


class Decorations(Fact):
	pass


class Tableware(Fact):
	pass


class Checklist(Fact):
	pass


class GuestsNumber(Fact):
	pass


class Date(Fact):
	pass


class PartyType(Fact):
	pass


class Budget(Fact):
	pass


class BudgetClass(Fact):
	pass


class HouseParty(Fact):
	pass


class Venue(Fact):
	pass


class Ages(Fact):
	pass


class Done(Fact):
	pass


class List:
	def __init__(self, lst):
		self.lst = []
		for item in lst:
			self.lst.append(item)

	def get_item(self, index):
		return self.lst[index]

	def set_item(self, index, new_value):
		self.lst[index] = new_value

	def get_list(self):
		return self.lst
