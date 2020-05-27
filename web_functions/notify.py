from notifiers import notify


def notify_me():
    notify('pushover', user='daniel.shackleton2009@gmail.com', token='bar', message='test')
