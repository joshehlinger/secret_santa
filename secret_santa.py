import argparse
import csv
import logging
import random
import smtplib
import sys
from datetime import datetime
from email import message


def main():
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('user',
                        help='App username for the gmail account')
    parser.add_argument('password',
                        help='App password for the gmail account')
    parser.add_argument('--dry-run',
                        dest='dry_run',
                        action='store_true',
                        help='Dont send emails, just test functionality')
    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(
        format='[%(asctime)-15s] %(levelname)-8s [%(name)s] %(message)s',
        level=logging.INFO,
        stream=sys.stdout)

    # Connect to gmail. Check out this support article
    # https://support.google.com/accounts/answer/185833?hl=en when this fails
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(args.user, args.password)

    # Get the Santas and shuffle em
    emails: list[dict] = []
    with open('emails.csv', 'r', newline='') as file:
        csvdict = csv.DictReader(file)
        for row in csvdict:
            emails.append(row)
    random.shuffle(emails)

    # Build the messages and send em
    for idx, santa in enumerate(emails):
        index = idx + 1
        target = emails[0] if index == len(emails) else emails[index]

        msg = message.Message()
        msg.add_header('From', args.user)
        msg.add_header('To', santa['email'])
        msg.add_header('Subject', f'Secret Santa {datetime.now().year}')

        msg_txt = (f"Ho ho ho, its {santa['name']}!\n\nHere's your secret "
                   f"santa recipient: {target['name']} \n\nHappy Holidays! "
                   "Please remember the gift should be about $25, or its "
                   "handmade equivalent. \n\nThey provided this "
                   f"note: {target['notes']}\n\n(This is an automated email "
                   "pls don't respond)\n\n")

        msg.set_payload(msg_txt)
        if args.dry_run:
            logging.info('Would send email to {}'.format(santa['email']))
            # Verify that it's a valid email
            server.verify(santa['email'])
        else:
            # Don't log the actual email here, b/c it's a secret (santa)!
            logging.info('Sending email')
            server.sendmail(args.user, santa['email'], msg.as_string())

    server.quit()
    logging.info('Finished sending')


if __name__ == '__main__':
    main()
