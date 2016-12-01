# -*- coding: utf8 -*-
import random
from sys import argv
__author__ = 'Elliot'

script, first = argv
class Namemaker(object):
	"""
	根治一个名字都想不出来的起名困难症，以及想到太多名字的选择困难症.
	"""
	def __init__(self, arg):
		super(Namemaker, self).__init__()
		self.arg = arg

	def create(self):
		choose_list = ['tom', 'jerry', 'lucy', 'lucky', 'Bob', 'Alice',]
		random.shuffle(choose_list)
		name_list = []
		if type(self.arg is str):
			self.arg = int(self.arg)
		for i in range(self.arg):
			name_list.append(choose_list[0])
			choose_list.pop(0)
		return name_list
		
if __name__ == '__main__':
	nm = Namemaker(first)
	print nm.create()
