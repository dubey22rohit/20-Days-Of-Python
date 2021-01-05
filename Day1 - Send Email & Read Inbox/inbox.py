import imaplib
import email

host = 'imap.gmail.com'
username = 'your_emailID'
password = 'password'

mail = imaplib.IMAP4_SSL(host)
mail.login(username,password)
mail.select('Inbox')
_,search_data = mail.search(None,'UNSEEN')
#print(search_data[0])
for num in search_data[0].split():
    email_data = {}
    #print(num)
    _,data = mail.fetch(num,'(RFC822)')
    #print(data[0])
    _,b = data[0]
    email_msg = email.message_from_bytes(b)
    for header in ['subject','to','from','date']:
        print("{} : {}".format(header,email_msg[header]))
        email_data[header] = email_msg[header]
    for part in email_msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(body.decode())
            email_data['body'] = body.decode()
        elif part.get_content_type() == "text/html":
            html_body = part.get_payload(decode=True)
            print(html_body.decode())
            email_data['html_body'] = html_body.decode()   
    #print(email_msg)
