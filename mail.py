import smtplib


sender_mail = "miholiayashmini@gmail.com"
sender_passwd = "jzwuowbrfnk "
recevier_mail = "ymiholia@gmail.com"
subject = "hello paji how are you"

s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login(sender_mail,sender_passwd)
s.sendmail(sender_mail,recevier_mail,subject)
s.quit()
