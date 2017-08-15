import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from getpass import getpass
import email
import os
import mimetypes

server = smtplib.SMTP()
server.connect("smtp.gmail.com",587)
server.ehlo()
server.starttls()
	

def init():

	email_id = raw_input("Gmail ID:") + "@gmail.com"
	password = getpass()

	## implement encrypted file storing this once entered
	
	server.login(email_id , password)

def send_email(name, email_id):
	fromaddr = 'Dhruv Singh'
	sub = 'Catching Up'
	X = 'dummy_subject'

	body = "Hi! How are you doing?\nJust wanted to catch up. Life is going well here. Hoping to know more about yours."

	body = body.replace("_name_", name)
	body = body.replace("_X_", X)

	fromaddr = 'Dhruv Singh'

	msg = email.MIMEMultipart.MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = email_id
	msg['Subject'] = sub
	msg.attach(MIMEText(body))

	server.sendmail(fromaddr,email_id,msg.as_string())


init()
send_email('DS','dhruvsinghiitb@gmail.com')
