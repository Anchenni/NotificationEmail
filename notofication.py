from re import M
import smtplib
from email.message import EmailMessage



def email_alert(subject,body, to):
	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to


	user = "lazyflous@gmail.com"
	msg["from"] = user
	password = "svwuvkdbnuwjblrm"

	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(user, password)
	server.send_message(msg)
	server.quit()

if __name__ == "__main__":
	try:
		file = open("emails.txt", 'r')
		mylist = list()
		for i in file:
			newstr = i.replace('\n',"")
			mylist.append(newstr)
		# print(mylist)	
		for j in mylist:
			email_alert("tuto python", "<html> <p style=\"color: red\">  hello word</p></html> ", j)
		print("Emain send")
	except:
		print("Error")