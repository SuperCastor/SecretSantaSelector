#! python

from sys import *
import random
import smtplib
from email.mime.text import MIMEText as text

print("> Please enter your gmail adress")
mail = input("$ ")
print("> Please enter your password")
password = input("$ ")

f = open(argv[1], "r")
file_output = []

for line in f:
    file_output.append(line[:-1])

person_array = []
person_data = []
for line in file_output:
    person_data.append(line.split(';')[1])
    person_data.append(line.split(';')[0])
    person_array.append(person_data.copy())
    person_data.clear()
random.shuffle(person_array)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(mail, password)

    for i in range (0, len(person_array) - 1):
        sent_from = mail
        msg = message = """\
Subject: Vous etes le Pere de Noel de ...

%s\n\nPas de contestation possible""" % (person_array[i + 1][0])
        server.sendmail(sent_from, person_array[i][1], msg)
    sent_from = mail
    msg = message = """\
Subject: Vous etes le Pere Noel de ...

%s\n\nPas de contestation possible""" % (person_array[0][0])
    server.sendmail(sent_from, person_array[len(person_array) - 1][1], msg)

except smtplib.SMTPException as e:
    print(e)
