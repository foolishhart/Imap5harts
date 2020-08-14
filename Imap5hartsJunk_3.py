import imaplib
import datetime

from email.parser import BytesParser

SpamTo = ['<malcolmmalcolm@5harts.com>','<ann@5harts.com>','<kim@5harts.com>','<noreply@5harts.com>','<kelsen@5harts.com>','<sales@5harts.com>','"ayden@5harts.com" <ayden@5harts.com>','ayden@5harts.com','<kirsty@5harts.com>','<kirst@5harts.com>', '<cat@5harts.com>', 'nickelsen@5harts.com']
subjectj = ['fungus','moncler']
SpamFrom = ['patelsheila', 'sheila patel']
tlds = ['.icu>', '.br>', '.bid>', '.date>', '.loan>', '.trade>', '.ga>', '.cf>' ,'.ml>', '.ar>', '.gq>','.tk>','.space>','.site>','.top>','.xyz>','patriotbundle.com','conservazon.com>']
tldsj = ['.icu>', '.br>', '.bid>', '.date>', '.loan>', '.trade>', '.ga>', '.cf>', '.ml>', '.ar>', '.gq>','.tk>', '.info>','.review>', '.online>','.website>','.space>','.site>','.top>','.win>','.life>','.xyz>','patriotbundle.com','conservazon.com>']
tldsj2 = ['.ltd>', 'americanas.com','.rest','.us>', '.pw>', '.press>', '.club>', '.live>', '.pro>', '.download>', '.xyz>' ,'.today>', '.casa>', '.world>','.live>','.id>','.site>']
goods = ['coursera', 'creditkarma', 'holidayextras', 'carbmanager', 'ntask', 'fool.co.uk', 'apple.com', 'evite.com', 'moneysavingexpert', 'edx.org', 'mailtoself', 'sourceforge', 'channel4', 'stubhub', 'bankofamerica', 'deloitte', 'trainline', 'cvsspecialty', 'halifax', 'priceline', 'heliohost', 'ticketmaster', 'lastpass', 'vintage-inns', 'mandsbank', 'spiritairlines', 'taxdisc', 'dds.ga', 'delta', 'upwork', 'telegraph', 'tvguide.co.uk', 'heathrow']
newss = ['nextdoor.com','nextdoor.co.uk', 'usps.gov', '@medium.com', 'dowjones.com', 'todoist.com', 'linkedin.com', 'tvguide.co.uk', 'realpython', 'cmwf.org', 'trello.com', 'thetimes.co.uk', 'nytimes.com', 'wsj.com', 'getpocket.com', 'pinterest.com', 'thepointsguy.co.uk', 'freecycle.org']
deleted=[]
now = datetime.datetime.now()
nowaware=now.replace(tzinfo=datetime.timezone.utc)
delta = datetime.timedelta(1)
delta2 = datetime.timedelta(2)
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
    resp,data = M.uid('fetch',uid,"(BODY[HEADER])")        
    msg = mailparser.parsebytes(data[0][1])
    print (msg['To'],msg['From'],msg['Subject'])
    for good in goods:
        if good in str(msg['From']).lower():
            result = M.uid('COPY', uid, 'Inbox')
            if result[0] == 'OK':
                M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
    #M.uid('STORE',uid, '-FLAGS', '(\\Seen)')
    if ('ashley' in str(msg['Subject']).lower() or 'ashley' in str(msg['From']).lower()) and ('madison' in str(msg['Subject']).lower() or 'madison' in str(msg['From']).lower()):
        M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
        deleted.append(str(msg['From'])+' '+str(msg['Subject']))
    for subj in subjectj:
    	if subj in str(msg['Subject']).lower():
    		M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
    		deleted.append(str(msg['From'])+' '+str(msg['Subject']))
    for tld in tldsj:
        if tld in str(msg['From']).lower():
            M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
            deleted.append(str(msg['From'])+' '+str(msg['Subject']))
    for tld in tldsj2:
        if tld in str(msg['From']).lower():
                result = M.uid('COPY', uid, 'Junk-Likely')
                if result[0] == 'OK':
                    M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
                    deleted.append(str(msg['From'])+' '+str(msg['Subject']))
    for spamf in SpamFrom:
        if spamf in str(msg['From']).lower():
            M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
            deleted.append(str(msg['From'])+' '+str(msg['Subject']))
    for spam in SpamTo:
        if spam in str(msg['To']).lower():
            M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
            deleted.append(str(msg['To'])+' '+str(msg['From'])+' '+str(msg['Subject']))
    try:
        if float(msg['X-Spam-Score'])> 4:
            result = M.uid('COPY', uid, 'Junk-HighSpam')
            if result[0] == 'OK':
                M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
    except:
        print ()
        
M.expunge()

M.select('Inbox')
resp, data = M.uid('search',None, "UNSEEN") # search and return Uids
uids = data[0].split()    
mailparser = BytesParser()
for uid in uids:
    resp,data = M.uid('fetch',uid,"(BODY[HEADER])")        
    msg = mailparser.parsebytes(data[0][1])
    print (msg['To'],msg['From'],msg['Subject'])
    
    for tld in tlds:
        if tld in str(msg['From']).lower():
            M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
            deleted.append(str(msg['From'])+' '+str(msg['Subject']))
    for tld in tldsj2:
        if tld in str(msg['From']).lower():
                result = M.uid('COPY', uid, 'Junk-Likely')
                if result[0] == 'OK':
                    M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
                    deleted.append(str(msg['From'])+' '+str(msg['Subject']))
    if str(msg['To']).lower() in SpamTo:
        M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
        deleted.append(str(msg['To'])+' '+str(msg['From'])+' '+str(msg['Subject']))
    M.uid('STORE',uid, '-FLAGS', '(\\Seen)')
if len(deleted)>0:
	f = open('deleted.txt','r+', encoding='utf-8')
	lines = f.readlines() # read old content
	f.close()
	f = open("deleted.txt", "w", encoding='utf-8') #Open file, overwriting existing file
	f.write(now.strftime("%A %Y-%m-%d %H:%M"+'\n')) #write to file
	for delete in deleted:
		f.write(delete+'\n.....\n')# write new content at the beginning
	f.write('\n\n') 
	for line in lines:
		f.write(line)# write old content after new
	f.close()
	
M.expunge()

M.select('"Inbox"')
resp, data = M.uid('search',None, "UNSEEN") # search and return Uids
unseenuids = data[0].split()
resp, data = M.uid('search',None, "ALL") # search and return Uids
uids = data[0].split()    
mailparser = BytesParser()
for uid in uids:
    resp,data = M.uid('fetch',uid,"(BODY[HEADER])")        
    msg = mailparser.parsebytes(data[0][1])
    for news in newss:
        if news in str(msg['From']).lower():
            print('yes' + ', '+msg['Date'])
            print (msg['To'],msg['From'],msg['Subject'])
            try:
                msgdate= datetime.datetime.strptime(msg['Date'][:31], '%a, %d %b %Y %H:%M:%S %z')
                if nowaware - msgdate > delta:
                    print (msg['Date'])
                    print (msg['Date'][:31])
                    M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
            except:
                print ('Error: '+msg['Date']+' '+msg['From'])
                print (msg['Date'][:31])
                try:
                    msgdate= datetime.datetime.strptime(msg['Date'][:30], '%a, %d %b %Y %H:%M:%S %z')
                    if nowaware - msgdate > delta:
                        print (msg['Date'])
                        print (msg['Date'][:30])
                        M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
                except:
                    print ('Error: '+msg['Date']+' '+msg['From'])
                    print (msg['Date'][:30])
                    try:
                        msgdate= datetime.datetime.strptime(msg['Date'][:25], '%a, %d %b %Y %H:%M:%S')
                        if datetime.datetime.now() - msgdate > delta2:
                            print (msg['Date'])
                            print (msg['Date'][:25])
                            M.uid('STORE',uid, '+FLAGS', '(\\Deleted)')
                    except:
                        print ('Error: '+msg['Date']+' '+msg['From'])
                        print (msg['Date'][:25])
     
                        
            
        if uid in unseenuids:
            	M.uid('STORE',uid, '-FLAGS', '(\\SEEN)')
M.expunge()

M.close()
M.logout()


