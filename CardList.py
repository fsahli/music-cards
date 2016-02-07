import csv
import os.path
import sys

class CardList:
	def __init__(self):
		self.path = os.path.dirname(os.path.realpath(__file__))
		self.cardList = self.readList()
		
	def readList(self):
		with open(self.path + '/cardList.csv', mode='r') as infile:
			reader = csv.reader(infile)
			cardList = {rows[0]:rows[1] for rows in reader}
			infile.close()
		return cardList
	
	def getPlaylist(self,card):
		self.cardList = self.readList()
		try:
			return self.cardList[card]
		except:
			print 'Card %s is not card list' % card
			return ''
	
	def addPlaylist(self, card, plist):
		try:
			if card not in self.cardList.keys():
				f = open(self.path + '/cardList.csv', 'a')
				f.write(card + ',' + plist + '\n')
				self.cardList[card] = plist
			else:
				print 'Card %s is already used' % card
		except:
			print 'Could not write file'
			if not os.path.isfile(self.path + '/cardList.csv'):
				print 'File cardList.csv does not exist'
			
			
			
