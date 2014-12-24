from readtest import *

while True:
        print 'Put the card in the reader'
        card=readCard()
        a=raw_input('Specify Spotify URI')
        if a=="q":
                break
        f=open('cardList.csv','a')
        f.write(card+','+a+'\n')
print "Exiting"

