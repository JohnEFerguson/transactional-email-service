# Jack Ferguson 2021
from app import Email, MailgunClient, SendgridClient

def test_mailgun_format_request(client):
    mailgun = MailgunClient()
    json = {
            "to": "Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>",
            "to_name": "john.everett.ferguson@gmail.com",
            "from": "Hellooooo",
            "from_name": "Testing some Mailgun awesomness!",
            "subject": "Testing some Mailgun awesomness!",
            "body": "Testing some Mailgun awesomness!"
            }
    email = Email(json)

    assert mailgun.build_request_body(email) == {
            "from": "Testing some Mailgun awesomness! <Hellooooo>",
            "to": ["Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>"],
            "subject": "Testing some Mailgun awesomness!",
            "text": "Testing some Mailgun awesomness!\n\n" 
            }

def test_sendgrid_format_request(client):
    sendgrid = SendgridClient()
    json = {
            "to": "Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>",
            "to_name": "john.everett.ferguson@gmail.com",
            "from": "Hellooooo",
            "from_name": "Testing some Mailgun awesomness!",
            "subject": "Testing some Mailgun awesomness!",
            "body": "Testing some Mailgun awesomness!"
            }
    email = Email(json)

    assert sendgrid.build_request_body(email) == {
                "personalizations": [{"to": [{"email": "Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>",
}]}],
                "from": {"email": "Hellooooo"},
                "subject": "Testing some Mailgun awesomness!",
                "content": [{"type": "text/plain", "value": "Testing some Mailgun awesomness!\n\n"}]
                }
