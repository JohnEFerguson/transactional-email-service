from flask import Flask
from flask import request as flask_request
from flask_expects_json import expects_json
import requests

email_schema = {
    'type': 'object',
    'properties': {
        'to': {'type': 'string'},
        'to_name': {'type': 'string'},
        'from': {'type': 'string'},
        'from_name': {'type': 'string'},
        'subject': {'type': 'string'},
        'body': {'type': 'string'}
    },
    'required': ['to', 'to_name', 'from', 'from_name', 'subject', 'body']
}

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route("/email", methods=['POST'])
@expects_json(email_schema)
def email():
    request_body = flask_request.json
    print(request_body)
    print(send_via_mailgun(
            to_email=request_body['to'],
            to_name=request_body['to_name'],
            from_email=request_body['from'],
            from_name=request_body['from_name'],
            subject=request_body['subject'],
            body=request_body['body']
            ))
    print(send_via_sendgrid(
            to_email=request_body['to'],
            to_name=request_body['to_name'],
            from_email=request_body['from'],
            from_name=request_body['from_name'],
            subject=request_body['subject'],
            body=request_body['body']
            ).text)
    
    return "<p>Hello, World!</p>"

def send_via_mailgun(to_email, to_name, from_email, from_name, subject, body):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org/messages",
		auth=("api", app.config['MAILGUN_API_KEY']),
		data={"from": "Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>",
			"to": ["john.everett.ferguson@gmail.com"],
			"subject": "Hellooooo",
			"text": "Testing some Mailgun awesomness!"})

def send_via_sendgrid(to_email, to_name, from_email, from_name, subject, body):
	return requests.post(
		"https://api.sendgrid.com/v3/mail/send",
        headers = {"Authorization": "Bearer {}".format(app.config['SENDGRID_API_KEY']), 'Content-Type': 'application/json'},
		json={"personalizations": [{"to": [{"email": "john.everett.ferguson@gmail.com"}]}],"from": {"email": "john.everett.ferguson@gmail.com"},"subject": "Sending with SendGrid is Fun","content": [{"type": "text/plain", "value": "and easy to do anywhere, even with cURL"}]})

