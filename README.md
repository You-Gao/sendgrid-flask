## use this solution instead for "free"
- so apparently you need a trusted smtp server to do what i was trying to do w/ the flask server...

### to send
- make a sendgrid api key and verify yourself w/ gmail
- to receive the email from above you can use a server for inbound parse or some other way to retrieve a post
- make sure to not have the link redirect checked in grid

### to receive
- set up mailforwarding to forwardemail.net
 
## tiger-daemon [deprecated]

- I have Github student dev so I get free hosting on Heroku, I have a domain I want to send and "receive" with.
- There aren't free services that aren't either only email forwarding to my inbox or to other inboxes.
- I didn't want to pay the $6 for Google workspace to manage an SMTP server for me.
- = my contrived solution

## Installation

### Prerequisite

- Python

### Set-Up

1. Clone the repository:
```
git clone https://github.com/You-Gao/sendgrid-flask.git
```

## Usage
1. flask run

## License
This project is licensed under the [Creative Commons CC0 1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/). See the [LICENSE](LICENSE) file for more details.


