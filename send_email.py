import smtplib, ssl

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "phumlanibrightdlamini@gmail.com"
    password = "agub ucpe rrpz jhfx"

    receiver = "phumlanibrightdlamini@gmail.com"

    context = ssl.create_default_context()

    message = """\
    Subject: Hi!
    How are you?
    Bye!"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver, message)