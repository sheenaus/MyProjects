import logging
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
logging.basicConfig(filename='example2.log', filemode='w', level=logging.DEBUG)
try:
    side_1 = -6
    side_2 = 5
    Rec_area = side_1 * side_2
    Rec_perimeter = 2 * (side_1 + side_2)
    print('Area of rectangle is : %d', Rec_area)
    logging.info('Area of rectangle is : %d', Rec_area)
    if (side_2 <= 0 or side_1 <= 0):
        print('warning')
        logging.warning('sides cannot be zero /negative side_1 :%d ; side_2 :%d ', side_1, side_2)
    print('Area of rectangle is :' + Rec_area)  # To show error
except TypeError as e:
    try:
        sender = 'fromuser@pythonlearning.com'
        logging.error('ERROR : %s', str(e))
        receivers = ['touser@pythonlearning.com']
        SUBJECT = str("SMTP e-mail test")
        TEXT = str(e)
        logfile='example2.log'
        with open(logfile) as fp:
            # Create a text/plain message
            msg = MIMEMultipart()
            msg.attach(MIMEText('test attachment'))
            with open(logfile, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                             )
                part['Content-Disposition'] = 'attachment; filename="%s"' % logfile
                msg.attach(part)
            #log_data=(fp.read())
            #msg.add_attachment(log_data)

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'The contents of %s' % logfile
        msg['From'] = 'fromuser@pythonlearning.com'
        msg['To'] =   'touser@pythonlearning.com'

        # Send the message via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
        print("success")
    except smtplib.SMTPException as e:
        print(e)

