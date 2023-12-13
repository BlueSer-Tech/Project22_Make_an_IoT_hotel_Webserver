import smtplib, ssl
from project_function import pin_random
from email.message import EmailMessage

def send_code(receiver_email):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "trandanghuy584@gmail.com"
    #receiver_email = "longxichlo485@gmail.com"
    password = "stch gftp tvuz jtjt"
    message = """
    Your PIN to get into the room: {}
    This is your private code, don't share it arbitrarily.""".format(pin_random())
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = "PIN CODE"
    msg['From'] = "trandanghuy584@gmail.com"
    msg['To'] = receiver_email
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        #server.sendmail(sender_email, receiver_email, message)
        server.send_message(msg)
#send_code("longxichlo485@gmail.com")