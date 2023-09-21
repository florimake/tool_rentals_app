### Gmail
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com' # gmail
# EMAIL_HOST_USER = 'arpad.python.test.app@gmail.com'    # your email address here, replace with yours!
# EMAIL_HOST_PASSWORD = '1985arpad1985'     # password of the above email account
# EMAIL_PORT = 587   # port for secure SMTP

### hotmail

""" 
https://outlook.live.com/mail/0/options/mail/accounts/popImap
SMTP setings:
Server name: smtp.office365.com
Port: 587
Encryption method: STARTTLS
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.office365.com' # hotmail
EMAIL_HOST_USER = 'arpad.python.test.app@hotmail.com'    # your email address here, replace with yours!
EMAIL_HOST_PASSWORD = '1985arpad1985'     # password of the above email account
EMAIL_PORT = 587   # port for secure SMTP