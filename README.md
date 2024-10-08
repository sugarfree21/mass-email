# Mass Email

## Intro

I created this collection of scripts using the yagmail library for when I need to send a large amount of emails and I don't want to do it manually. 

## Quick Explanation of Files

- `massemail.py` - Actual script for sending out emails
- `env.py` - Location for your gmail app password (definitely include this in your .gitignore)
- `combine.py` - A script I wrote for a unique situation where I had to combine two csv files of contacts
- `test.csv` - List of email targets with names and emails
- `test_subject.txt` - Subject line of email
- `test_content.txt` - Actual content of email. Can be HTML formatted if you're looking for that.