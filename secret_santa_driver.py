import json
import os
import random
import smtplib
from datetime import datetime
from email import message
from itertools import cycle

from dotenv import load_dotenv


def main():
    load_dotenv()

    server = smtplib.SMTP('smtp.gmail.com:587')

    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    dry_run = eval(os.getenv("DRY_RUN", True))

    with open('emails.json') as emails:
        email_to_name_dict = json.load(emails)

    santas = random.sample(email_to_name_dict.items(), len(email_to_name_dict))
    targets = cycle(santas)
    next(targets)

    server.ehlo()
    server.starttls()
    server.login(username, password)

    for (santa_email, santa_name), (target_email, target_name) in zip(santas, targets):
        msg = message.Message()

        msg.add_header('From', username)
        msg.add_header('To', target_email)
        msg.add_header('Subject', f'Secret Santa {datetime.now().year}')

        msgText = f"Ho ho ho, its {santa_name}!\n\nHere's your secret santa recipient: {target_name}" \
                  "\n\nHappy Holidays! Please remember the gift should be about $20, or " \
                  "its handmade equivalent.\n\n\n\n(This is an automated email)\n\n"

        msg.set_payload(msgText)
        if dry_run == False:
            server.sendmail(username, santa_email, msg.as_string())

    server.quit()
    print('\nits over!')


if __name__ == '__main__':
    main()
