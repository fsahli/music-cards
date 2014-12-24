#!/usr/bin/env python
from mpd import MPDClient
from readtest import *
import re

while True:
	try:
		card = readCard()
		cardList = readList()
		plist=cardList[card]
		client = MPDClient()               # create client object
		client.timeout = 10                # network timeout in seconds (floats allowed), default: None
		client.idletimeout = None  
		print "Connecting..."
		client.connect("localhost", 6600) 
		print "Connected!"
		if plist=='pause':
			client.pause()
		else:
			client.stop()
			client.clear()
			client.add(plist)
			if re.search('playlist',plist):
				client.shuffle()
			client.play()
		client.close()
	except:
		pass
