import smtplib
from email.encoders import encode_base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def send(sender, receiver, subject, body, image=None):
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    text = MIMEText(body, "plain")

    message.attach(text)

    if image:
        image.seek(0)
        file = MIMEBase('application', "octet-stream")
        file.set_payload(image.read())
        encode_base64(file)
        file.add_header('Content-Disposition',
                        'attachment; filename="rain.png"')
        message.attach(file)

    server = smtplib.SMTP("smtp.mailtrap.io", 2525)
    server.login("2ff5f8d9b897ae", "86e4d0018894a2")
    server.sendmail(sender, receiver, message.as_string())
    server.quit()
