import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

message = Mail(from_email='kanavraina11@gmail.com',
                to_emails='kanavraina98@gmail.com',
                subject='Sending with twilio sendgrid',
                plain_text_content='testing with Twilio',
                html_content='<h1>hello sendgrid</h1>'
)

try:
    sg=SendGridAPIClient('ADD YOUR API KEY HERE')
    response=sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
'''
Create an account on sendgrid
GO to Settings
Create API keys
Save this api key in .env file
Create a sender('https://app.sendgrid.com/settings/sender_auth/senders')
now run this file if you get 202 response email sent successfully
'''
