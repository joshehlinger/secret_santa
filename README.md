# Secret Santa

Ho ho ho!

Uses a gmail account and a CSV file to randomize and send secret
santa assignments. Keep in mind that if you send emails from gmail you'll
need to set up an App Password - https://support.google.com/accounts/answer/185833?hl=en

A 5/10 on the Jank Scale.

## Configuration

Run with `python secret_santa.py APP_USERNAME APP_PASSWORD`

Use the provided `--dry-run` option to test this without actually sending a bunch of emails

The emails themselves should be put into a file in the root of the
directory called `emails.csv`. This should have three headers, `name,email,notes`

```
name,email,notes
A Name,email@gmail.com,Please dont get me any socks
Homer Simpson,k.email.yes@gmail.com,More donuts please!
Another Person,stillanemail@gmail.com,"Make sure, that you, escape commas"
```

To prevent couples from getting each other as secret santa recipients, create a `couples.json` file.
For normalization reasons, keep it all lowercase:

```json
[
  ["romeo", "juliet"],
  ["bonnie", "clyde"],
  ["mickey", "minnie"]
]
```