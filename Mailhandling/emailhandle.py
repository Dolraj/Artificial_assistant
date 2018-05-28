import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "grishma9393@gmail.com"
toaddr = "drrijal94@gmail.com"
msg = MIMEMultipart()
msg['From'] = "grishma9393@gmail.com"
msg['To'] = "drrijal94@gmail.com"
msg['Subject'] = "SUBJECT OF THE MAIL"
 
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("grishma9393@gmail.com", "grishma9847109441")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

