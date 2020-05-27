from web_functions import notify
from web_functions import page_model


def check_grouse():
    header = page_model.get_header()
    statement = 'Operations suspended'
    try:
        if statement not in header.text or not header:
            notify.send_notification()
    except AttributeError:
        notify.send_notification()


if __name__ == '__main__':
    check_grouse()
