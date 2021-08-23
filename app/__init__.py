# Jack Ferguson 2021
# in the future the app can be refactored into a class
from flask import Flask, Response, abort, request as flask_request
from flask_expects_json import expects_json
from .email import Email
from .mailgun import MailgunClient 
from .sendgrid import SendgridClient 

## this can be extended with more specific types with regex for increased security
EMAIL_REQUEST_SCHEMA = {
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


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    mailgun = MailgunClient() ## load additional configuration here 
    sendgrid = SendgridClient()

    ## requests should be authenticated
    @app.route("/email", methods=['POST'])
    @expects_json(EMAIL_REQUEST_SCHEMA)
    def post_email():
        try:
            request_body = flask_request.json
            email = Email(request_body=request_body)

            # switching like this is not a scalable approach, but is sufficient for now
            if app.config['TESTING']: 
                ## for tests just return 200
                ## this would be updated when we can support better integration testing
                return Response(status=200) 
            elif app.config['USE_MAILGUN']:
                response = mailgun.send_via_mailgun(email=email, api_key=app.config['MAILGUN_API_KEY'])
            else:
                response = sendgrid.send_via_sendgrid(email=email, api_key=app.config['SENDGRID_API_KEY'])

            if response.status_code in [200, 202]: # 200 for mailgun, 202 for sendgrid
                return Response(status=200) 
            else:
                ## something went wrong with 3rd party integration
                ## here we should log what went wrong so that issue can be addressed
                abort(500)

        except:
            # should catch specific exception, log what happened
            abort(500)

    return app
