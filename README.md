# can-i-hike-yet
This simple script checks the Grouse Mountain website to see if operations are still cancelled, and notifies the user if there have been any updates. Scheduled runs in docker on private server.

## Built With
- Selenium WebBrowser
- smtplib

## Requirements
1. If you don't have one already, set up a gmail account and create a new application password (under account security)

2. Either create a file called `credentials.py` which contains the following string variables within the web_functions package, or simply add these variables to `notify.py`:
- `username` - set this as your gmail email address
- `password` - set this as your application password created in step one
- `recipient` - set this as the recipient email address 


## Usage
After changing user credentials in either `credentials.py` or `notify.py`, schedule `main.py` to run automatically using crontab or another scheduler.
