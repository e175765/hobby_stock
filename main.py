from src import get_name
from src import test_gmail

get_name.get()
gmail_account = 'otn5m44148w@gmail.com'
gmail_password = '1998-0911-Hiroto'
mail_to = 'otn5m44148w@gmail.com'
subject = "メール送信テスト"
path = 'data/sample.csv'
text = test_gmail.read_text(path)
test_gmail.make_mail(gmail_account,gmail_password,mail_to,subject,text)