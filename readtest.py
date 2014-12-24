import string
import csv

from evdev import InputDevice
from select import select

keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
dev = InputDevice('/dev/input/event1')
	
def readCard():
	stri=''
	nchar=0

	while nchar<11:
	   r,w,x = select([dev], [], [])
	   for event in dev.read():
		if event.type==1 and event.value==1:
			stri+=keys[ event.code ]
			print( keys[ event.code ] )
			nchar+=1
	return stri[0:10]

def readList():
	with open('/home/fsahli/Box/cardList.csv', mode='r') as infile:
		reader = csv.reader(infile)
		cardList = {rows[0]:rows[1] for rows in reader}
		infile.close()
	return cardList
