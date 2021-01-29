import datetime as dt
import time
# import smtplib
import  smtplib,getpass

# def send_email():
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login('My Gmail ID', 'My password')
#     message = 'sending this from python!'
#     server.sendmail('My Gmail ID', 'Recipient')
#     server.quit()

# send_time = dt.datetime(2019,12,20,4,25,0) # set your sending time in UTC
# print(send_time.timestamp())
# print(time.time())
# print(time.sleep(send_time.timestamp() - time.time()))
# send_email()
# _email_usingSMTPLIB.py 
#created_on:10-November-2020
#created_by:Victor NKuna
#Email:victor.nkuna@yahoo.com

send_object = smtplib.SMTP("smtp.gmail.com",587)

sender_email_address="victornkuna37@gmail.com"
receiver = "victor.nkuna@yahoo.com"
password = input("Please enter the password:\n")
# ssl.create_default_context()

send_object.starttls()

send_object.login(sender_email_address,password)

message = """\

Subject: Send using smtplib from python

Hello your using python to send a  an emall

assert=='test"


"""

try:
    send_object.sendmail(sender_email_address,receiver,message)
    print("Successfully sent email")


except Exception as e:
    print(e)
    print("Unable to send the email")
finally:
    send_object.quit()
