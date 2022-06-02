import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'b69c047df7fecd'
    password = 'c805e5fbb172b3'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li>" \
              f"<li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'bcars@test.com'
    reciever_email = 'delernestoa@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Bcars Feedback'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())
