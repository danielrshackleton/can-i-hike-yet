import smtplib
from web_functions.credentials import recipient, username, password


def send_notification():
    # Mail template for registration notification email
    subject = "Grouse is back open!"
    body = "Get off your fat ass, it's time to go hiking!"
    # recipient = 'test@gmail.com' - insert recipient email address here

    msg = 'Subject: {0}\n\n{1}'.format(subject, body)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, recipient, msg)
    server.quit()
    return True


if __name__ == '__main__':
    send_notification()
