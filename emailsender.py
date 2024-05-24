import smtplib   #communitate with our smpt server witch are use on mainly services like gmail, yahoo, email services.

to = input("Enter the email of recipent:\n")   #user input

content = input("Enter the content for mail:\n")   # user input

def sendEmail(to, content):  #function in function we are passing two values.
    server = smtplib.SMTP('smtp.gmail.com', 587)   # passing smtp server address and also a port numberfor sending a email.
    server.ehlo()  # try to make a communication between smtp server or gmail.
    server.starttls()   # to start a session.
    server.login('senderemail@gmail.com','123')  # write the sender email address and then the password of the user. 
    server.sendmail('senderemail.com@gmail.com', to, content)   #
    
    server.close()

sendEmail(to, content)











    
