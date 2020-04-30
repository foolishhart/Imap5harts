import imaplib
import datetime
import re
import string
from email.parser import BytesParser
import email
import mailbox

SpamTo = ['<malcolmmalcolm@5harts.com>','<ann@5harts.com>','<kim@5harts.com>','<noreply@5harts.com>','<kelsen@5harts.com>','<sales@5harts.com>','"ayden@5harts.com" <ayden@5harts.com>','ayden@5harts.com','<kirsty@5harts.com>','<kirst@5harts.com>', '<cat@5harts.com>', 'nickelsen@5harts.com']
subjectj = ['fungus','moncler']
SpamFrom = ['patelsheila', 'sheila patel']
tlds = ['.icu>', '.br>', '.bid>', '.date>', '.loan>', '.trade>', '.ga>', '.cf>' ,'.ml>', '.ar>', '.gq>','.tk>','.space>','.site>','.top>','.xyz>','patriotbundle.com','conservazon.com>']
tldsj = ['.icu>', '.br>', '.bid>', '.date>', '.loan>', '.trade>', '.ga>', '.cf>', '.ml>', '.ar>', '.gq>','.tk>', '.info>','.review>', '.online>','.website>','.space>','.site>','.top>','.win>','.life>','.xyz>','patriotbundle.com','conservazon.com>']
tldsj2 = ['.ltd>', '.us>', '.pw>', '.press>', '.club>', '.live>', '.pro>', '.download>', '.xyz>' ,'.today>', '.casa>', '.world>','.live>','.id>','.site>']
goods = ['coursera', 'creditkarma', 'holidayextras', 'carbmanager', 'ntask', 'fool.co.uk', 'apple.com', 'evite.com', 'moneysavingexpert', 'edx.org', 'mailtoself', 'sourceforge', 'channel4', 'stubhub', 'bankofamerica', 'deloitte', 'trainline', 'cvsspecialty', 'halifax', 'priceline', 'heliohost', 'ticketmaster', 'lastpass', 'vintage-inns', 'mandsbank', 'spiritairlines', 'taxdisc', 'dds.ga', 'delta', 'upwork', 'telegraph', 'tvguide.co.uk', 'heathrow']
newss = ['nextdoor.co.uk', 'usps.gov', '@medium.com', 'dowjones.com', 'todoist.com', 'linkedin.com', 'tvguide.co.uk', 'realpython', 'cmwf.org', 'trello.com', 'thetimes.co.uk', 'nytimes.com', 'wsj.com', 'getpocket.com', 'pinterest.com', 'thepointsguy.co.uk', 'freecycle.org']
now = datetime.datetime.now()
handle = []
M = imaplib.IMAP4('mail.livemail.co.uk',143)
f=open(".account.txt","r")
lines=f.readlines()
username=lines[0]
password=lines[1]
f.close()
M.login(username[0:18], password)     
M.select('"Junk Email"')
resp, data = M.uid('search',None, "ALL") # search and return Uids


uids = data[0].split()    
mailparser = BytesParser()
for uid in uids:
    #resp,data = M.uid('fetch',uid,'(RFC822)')
    resp,data = M.uid('fetch',uid,"(BODY[TEXT])")
    msg = mailparser.parsebytes(data[0][1])
    #print (msg)
    print (data[0][1])

'''
for uid in uids:
    #resp,data = M.uid('fetch',uid,'(RFC822)')
    resp,data = M.uid('fetch',uid,"(BODY[HEADER])")
    msg = mailparser.parsebytes(data[0][1])
    #msg = str(data[0][1])
    domain = msg['From'].split('@') 
    try:
        #handle.append(msg)
        handle.append(domain[1])
        #print (domain[0])
    except:
        print ('Error: '+domain[0])
'''
	
M.expunge()

M.close()

M.logout()
'''
counts=dict()

for line in handle:
	words = line.lower().split()
	stuff = re.findall('([a-zA-Z_0-9äöüÄÖÜßçêã]+)', line)
	for word in stuff:
		if word.islower():
			if (word not in counts):
				counts[word] = 1
			else:
				counts[word] += 1
	for word in stuff:
		if word.istitle():
			if word.lower() in counts:
				counts[word.lower()] += 1
			else:		 
				if word not in counts:
					counts[word] = 1
				else:
					counts[word] += 1

#for kee,val in counts.items():
    #if val > 30 and len(kee)>3: 
        #maxval=val
        #maxkee=kee
        
		#print kee,val
    #else: continue 
l = list()
for key, val in counts.items():
	if len(key)>1:
		l.append( (val, key))
l.sort(reverse=True)
#for key, val in l[:150] :
for key, val in l :
	if key >=1: print (key, val)
			#print counts['patient']
print (len(counts))
print (len(words))
'''
