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

    if image:
        image.seek(0)
        file = MIMEBase('application', "octet-stream")
        file.set_payload(image.read())
        encode_base64(file)
        file.add_header('Content-Disposition', 'attachment; filename="rain.png"')
        file.add_header('Content-ID', '<rain>')
        message.attach(file)

        html = MIMEText(f'<div>{body}</div><img src="cid:rain">', 'html')
        message.attach(html)

    else:
        text = MIMEText(body, "plain")
        message.attach(text)


    server = smtplib.SMTP("smtp.mailtrap.io", 2525)
    server.login("849fe1684e3d78", "dd589f2c09b940")
    server.sendmail(sender, receiver, message.as_string())
    server.quit()
