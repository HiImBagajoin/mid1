import smtplib
from email.mime.text import MIMEText

smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
x = smtpobj.ehlo()
print(type(x))
print(str(x))
msg = MIMEText( 'Awesome \nIt works')
msg['subject'] = 'Test'
msg['from'] = 'tolovetolove5252@gmail.com'
msg['to'] = 'donottrytohackme87@gmail.com'
smtpobj.login('tolovetolove5252@gmail.com', 'qAzWsX1/.2:,')
smtpobj.send_message(msg)
smtpobj.quit()