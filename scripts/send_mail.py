from flask_mail import Mail, Message
from flask import render_template
import random

VC = "./verification_code.html"


class Mailer:

    def __init__(self, app):
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        app.config['MAIL_USERNAME'] = 'infinote.app.adteam@gmail.com'
        app.config['MAIL_PASSWORD'] = 'mloyicqrfydnebaw'
        self.mail = Mail(app)
        self.code = []

    def send_verification_code(self, subject, sender, recipients_list, message):
        msg = Message(subject, sender=sender, recipients=recipients_list)
        self.code.clear()
        for i in range(6):
            self.code.append(random.randint(0, 9))
        code = self.code
        msg.html = str(render_template(VC, email_msg=message, d1=str(code[0]), d2=str(code[1]),
                                       d3=str(code[2]), d4=str(code[3]), d5=str(code[4]), d6=str(code[5])))
        self.mail.send(msg)
        return "done"

    def send_message(self, subject, sender, recipients_list, message):
        msg = Message(subject, sender=sender, recipients=recipients_list)
        self.code.clear()
        msg.html = message
        self.mail.send(msg)
        return "done"

    def send_issue_message(self, name, email, message):
        msg = Message("ISSUE - " + email, sender='infinote.app.adteam@gmail.com', recipients=['infinote.app.adteam'
                                                                                              '@gmail.com'])
        msg.html = name + ": " + message
        self.mail.send(msg)
        return "done"
