from web_functions import notify
from web_functions import page_model
from notifiers import notify


def check_grouse():
    header = page_model.get_header()
    statement = 'Operations suspended'
    if statement not in header.text and header:
        _notify_me()


def _notify_me():
    _message = "Get off your ass, it's time to go hiking!"
    _recipient = 'daniel.shackleton2009@gmail.com'
    notify('pushover', user=_recipient, token='bar', message=_message)
    print(_message)


if __name__ == '__main__':
    # _notify_me()
    check_grouse()
