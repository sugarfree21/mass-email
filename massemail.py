from env import APP_PASS
import yagmail
import csv

sender = 'john@example.com'
alias = 'John Doe'
password = APP_PASS

subjectfile = open('test_subject.txt', 'r')
emailsubject = subjectfile.read()
subjectfile.close()

contentfile = open('test_content.txt', 'r')
content = contentfile.read()
contentfile.close()

targetfile = open('interested_dds.csv', 'r')
targetcsv = csv.reader(targetfile)

with yagmail.SMTP({sender : alias}, password) as yag:
    for target in targetcsv:
        personalcontent = content.format(fname=target[0], lname=target[1])
        yag.send(to=target[2], cc='jane@example.com', subject=emailsubject, contents=personalcontent)