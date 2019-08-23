
import os
import smtplib

#

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#print(f'EMAIL_ADDRESS={EMAIL_ADDRESS}')
#print(f'EMAIL_PASSWORD={EMAIL_PASSWORD}')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject = 'mary had a little lamb'
    body = 'its fleece was white as snow. everywhere mary went the lamb was sure to go'

    msg = f'Subject: {subject}\n\n{body}'
    
    smtp.sendmail(EMAIL_ADDRESS,'terry.cadd@gmail.com',msg)

    
    
    
