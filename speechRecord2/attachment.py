import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
email_user='noreplysupermaids@gmail.com'
email_send='suyashkholapure1996@gmail.com'
subject = 'WARNING'
msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_send
msg['subject']=subject
body ="HI PARENTS THIS MAIL IS INFORM YOU THAT YOUR CHILD WATCHING SOME BAD CONTENT VIDEO"

msg.attach(MIMEText(body,'plain'))

filename='Offensive.txt'
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename="+filename)

msg.attach(part)
text=msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'complaint123')

server.sendmail(email_user,email_send,text)
server.quit()