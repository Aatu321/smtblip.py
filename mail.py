import smtplib


sender_mail = "xyz@gmail.com"
sender_passwd = "hehhehhe "
recevier_mail = "zyx@gmail.com"
subject = "hello paji how are you"

s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login(sender_mail,sender_passwd)
s.sendmail(sender_mail,recevier_mail,subject)
s.quit()
