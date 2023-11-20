import json
import os
import random
import smtplib
from datetime import datetime
from email import message

from dotenv import load_dotenv


def main():
    load_dotenv()

    server = smtplib.SMTP('smtp.gmail.com:587')

    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    dry_run = eval(os.getenv("DRY_RUN", True))

    server.ehlo()
    server.starttls()
    server.login(username, password)

    with open('emails.json') as emails:
        email_list = list(json.load(emails).items())

    random.shuffle(email_list)

    for idx, (santa_name, santa_email) in enumerate(email_list):
        index = idx + 1
        if index == len(email_list):
            target_name = email_list[0][0]
        else:
            target_name = email_list[index][0]

        msg = message.Message()
        msg.add_header('From', username)
        msg.add_header('To', santa_email)
        msg.add_header('Subject', f'Secret Santa {datetime.now().year}')

        msg_txt = f"Ho ho ho, its {santa_name}!\n\nHere's your secret santa " \
                  f"recipient: {target_name} \n\nHappy Holidays! Please " \
                  "remember the gift should be about $25, or its " \
                  "handmade equivalent.\n\n\n\n" \
                  "(This is an automated email pls don't respond)\n\n"

        msg.set_payload(msg_txt)
        if not dry_run:
            server.sendmail(username, santa_email, msg.as_string())

    server.quit()
    print('\nits over!')


if __name__ == '__main__':
    main()
