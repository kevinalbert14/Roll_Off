import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


def emailer(rece):

    sender = 'keevviin97@gmail.com'
    password = 'xeqgjplbmqqtpbsm'
    receiver = rece
    message = 'The message here'
    file_location = 'C:\\Users\\keevv\\Desktop\\Roll_Off\\valid.html'

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = password
    msg['Subject'] = 'Report'
    msg.attach(MIMEText(message, 'plain'))


    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()