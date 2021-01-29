from flask_mail import Mail,Message
from flask import  Flask, redirect,url_for,request

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] ="victornkuna37@gmail.com"
app.config["MAIL_PASSWORD"] = "********"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] =True

#lets create an instacne of the mail classes

mail = Mail(app)

"""
message object is set in a python function that is mapped by the URL rule '/'


"""

@app.route("/")
def messageObject():
    msg =Message("Hello",sender="victornkuna37@gmail.com",
    recipients=["victor.nkuna@yahoo.com"])
    msg.body = "This is the mail body"

    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)
