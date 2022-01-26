import smtplib
from email.message import EmailMessage
import logging

def send_simple_message(mailtext, mailhtml, month, files=None):
    # print("file is:" + filename)
    logging.basicConfig(level=logging.DEBUG)
    import smtplib
    from os.path import basename
    from email.mime.application import MIMEApplication
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.header import Header
    from email.utils import formataddr
    Recipient = "me@domain.com"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Summary of Credit Card payments due in " + month
    msg['From'] = formataddr((str(Header('Finance Manager', 'utf-8')), 'creditcards@domain.in'))
    msg['To']      = Recipient
    part1 = MIMEText(mailtext, 'plain')
    part2 = MIMEText(mailhtml, 'html')
    msg.attach(part1)
    msg.attach(part2)
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    s = smtplib.SMTP('smtp.mailgun.org', 587)
    s.login('postmaster@domain.in', 'pass')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit() 