import smtplib

# Your email account credentials
sender_email = "sender@example.com"
sender_password = "sender_email_password"

# Receiver email
receiver_email = "receiver@example.com"

# Email content
message = """
Subject: Simple Test Email

This is a test email message."""

# Connect to the server and send email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587) # Gmail SMTP server
    server.ehlo()
    server.starttls()
    server.login('ababatunde022@gmail.com', 'azdsaxkgfhegcozh')
    server.sendmail('ababatunde022@gmail.com', 'tundeadegoke06@gmail.com', message)
    print ('Email sent!')
except Exception as e:
    print ('Something went wrong...', e)
finally:
    server.quit()
