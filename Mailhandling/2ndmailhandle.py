import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("grishma9393@gmail.com", "grishma9847109441")
 
msg = "voiced controlled digital assistant"
server.sendmail("grishma9393@gmail.com", "drrijal94@gmail.com", "voiced controlled digital assistant")
server.quit()

