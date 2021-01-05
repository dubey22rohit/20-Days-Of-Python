import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
username = 'your_emailID'
password = 'password'

def send_mail(text='Email Body', subject='Hello SMTP', from_email="Hanzo Hasashi <mortalkombatrohit22@gmail.com>", to_emails=None ,html = None):
    assert isinstance(to_emails, list)
    #Creating mail contents
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = " ,".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText("<h1>This is working!!</h1>",'html')
        msg.attach(html_part)

    msg_str = msg.as_string()
    # login to SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()

send_mail(to_emails= ['mortalkombatrohit22@gmail.com','rohu.billu22@gmail.com'])