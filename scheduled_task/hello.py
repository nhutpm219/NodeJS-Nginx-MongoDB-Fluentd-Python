import subprocess, smtplib, ssl

FAILED_TIMES = subprocess.check_output("cat /var/log/buffer.*.log | grep -v -e  200 -e 'fluent.info' | wc -l", shell=True)
FAILED_TIMES = str(FAILED_TIMES)
FAILED_TIMES = FAILED_TIMES[:-3]
FAILED_TIMES = int(FAILED_TIMES[2:])
print ("Failed: ", FAILED_TIMES)

#port = 587  # For starttls
#smtp_server = "smtp.gmail.com"
#sender_email = "nhutpm219@gmail.com"
#receiver_email = "tranvanrua751@gmail.com"
#password = input("Type your password and press enter:")
#message = """\
#Subject: Hi there

#This is alert about has over 10 times try to access but failed, was sent from Python."""


if FAILED_TIMES >= 10:
    print ("A email will be sent")
#    context = ssl.create_default_context()
#    with smtplib.SMTP(smtp_server, port) as server:
#        server.starttls(context=context)
#        server.login(sender_email, password)
#        server.sendmail(sender_email, receiver_email, message)
else:
    print ("do nothing")


