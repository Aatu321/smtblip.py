
import smtplib


sender_mail = "xyz@gmail.com"
sender_passwd = "hehehe "
recevier_mail = "zxy@gmail.com"
subject = "hello paji how are you"

s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login(sender_mail,sender_passwd)
s.sendmail(sender_mail,recevier_mail,subject)
s.quit()
