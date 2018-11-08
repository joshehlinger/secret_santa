# Secret Santa

Ho ho ho!

Uses a gmail account and a json file to randomize and send secret
santa assignments

A 5/10 on the Jank Scale.

## Development

Developed on Python 3.7

Create a virtual environment and

`pip install -r requirements.txt`

## Configuration

This script uses a utility called python-dotenv to populate important
environment variables. Create a file at the root of the directory
called `.env` and populate it with your email credentials, and a flag
called DRY_RUN set to `False` so the script will send emails:

```
EMAIL_USERNAME='email.to.send.from@gmail.com'
EMAIL_PASSWORD='supersecret'
DRY_RUN=False
```

The emails themselves should be put into a file in the root of the
directory called `emails.json`. This is a simple json object with a mapping
of `email:name`, like the following:

```
{
    "email@gmail.com": "A Name",
    "anotheremail@gmail.com": "Totally Real",
    "k.email.yes@gmail.com": "Homer Simpson",
    "stillanemail@gmail.com": "Another Person"
}
```