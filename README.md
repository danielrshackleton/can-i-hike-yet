# Can I hike yet?
This simple script checks the Grouse Mountain website to see if operations are still cancelled, and notifies the user if there have been any updates. Scheduled runs in docker on private server.

## Built With
- Selenium WebBrowser
- WebDriverManager
- smtplib

## Requirements
- Pipenv must be installed on your machine -> `pipenv run python check_website.py` to install dependencies from `Pipfile`
- Must have a browser of some kind (eg. Chrome, Firefox etc.)
- You need an email account/SMTP server
##### Gmail example:
Set up a Gmail account and create a new application password (under account security). 

2. Either create a file called `credentials.py` which contains the following string variables within the web_functions package, or simply add these variables to `notify.py`:
- `username` - set this as your gmail email address
- `password` - set this as your application password created in step one
- `recipient` - set this as the recipient email address 



## Usage
After changing user credentials in either `credentials.py` or `notify.py`, schedule `main.py` to run automatically using cron or another scheduler.

##### NOTE: ChromeDriver/GeckoDriver etc. not needed, only the browsers themselves need be installed.
