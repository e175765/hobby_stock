import smtplib, ssl
from email.mime.text import MIMEText
import csv

gmail_account = 'otn5m44148w@gmail.com'
gmail_password = '1998-0911-Hiroto'

mail_to = 'otn5m44148w@gmail.com'

subject = "メール送信テスト"
def make_mail(account, password, to_parson, sub, text):
    gmail_account = account
    gmail_password = password
    mail_to = to_parson
    subject = sub
    body = text
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail_account
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg) # メールの送信                                         
#print("ok.")
#body = "メール送信テスト"

def read_text(path):
    with open(path) as f:
        s = f.readlines()
        #body = s[0]
    text = ''
    for data in s:
        text += data+'\n' 
    return text

