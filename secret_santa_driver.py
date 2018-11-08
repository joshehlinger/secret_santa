import os
import smtplib
import random
import json
from email import message
from dotenv import load_dotenv


def main():
    load_dotenv()

    server = smtplib.SMTP('smtp.gmail.com:587')

    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    dry_run = eval(os.getenv("DRY_RUN", True))

    with open('test_emails.json') as emails:
        email_to_name_dict = json.load(emails)
        email_list = list(email_to_name_dict.keys())

    random.shuffle(email_list)

    server.ehlo()
    server.starttls()
    server.login(username, password)

    for x in range(len(email_list)):
        msg = message.Message()

        if x == len(email_list) - 1:
            theTarget = email_to_name_dict[email_list[0]]
        else:
            theTarget = email_to_name_dict[email_list[x + 1]]
        theSanta = email_to_name_dict[email_list[x]]

        msg.add_header('From', username)
        msg.add_header('To', email_list[0])
        msg.add_header('Subject', 'Secret Santa 2017')

        msgText = "Ho ho ho, its " + theSanta + "!\n\nHere's your secret santa recipient: " + theTarget + \
                  "\n\nHappy Holidays! Please remember the gift should be about $20, or " + \
                  "its handmade equivalent.\n\n\n\n(This is an automated email)\n\n"

        msg.set_payload(msgText)
        if dry_run == False:
            server.sendmail(username, email_list[x], msg.as_string())

    server.quit()
    print('\nits over!')


if __name__ == '__main__':
    main()