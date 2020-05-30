from web_functions import notify
from web_functions import page_model


def check_grouse():
    header = page_model.get_header()
    closed = 'closed until further notice'
    if closed not in header:
        print('Grouse now open. Sending Notification...')
        notify.send_notification()
        print('Notification Sent.')


if __name__ == '__main__':
    check_grouse()
