from web_functions import notify
from web_functions import page_model


def check_grouse():
    header = page_model.get_header()
    try:
        if 'COVID-19' not in header or not header:
            print(header)
            notify.send_notification()
    except AttributeError:
        notify.send_notification()


if __name__ == '__main__':
    check_grouse()
