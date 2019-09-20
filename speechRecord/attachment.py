import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
email_user='Enter sender email'
email_send='Enter receiver email'
subject = 'WARNING'
msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_send
msg['subject']=subject
body ="HI PARENTS THIS MAIL IS INFORM YOU THAT YOUR CHILD WATCHING SOME BAD CONTENT VIDEO"

msg.attach(MIMEText(body,'plain'))

filename='record.txt'
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename="+filename)

msg.attach(part)
text=msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'enter sender email password')

server.sendmail(email_user,email_send,text)
server.quit()