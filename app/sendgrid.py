# Jack Ferguson 2021
import requests

class SendgridClient:

    ## this should be configured
    _base_url = 'https://api.sendgrid.com/v3/mail/send'
    
    ## this is the only part it really makes sense to unit test
    def build_request_body(self, email):
        return {
                "personalizations": [{"to": [{"email": email.to_email}]}],
                "from": {"email": email.from_email},
                "subject": email.subject,
                "content": [{"type": "text/plain", "value": email.body}]
                }

    # not covered by unit tests
    def send_via_sendgrid(self, email, api_key):
        return requests.post(
                self._base_url,
                headers = {"Authorization": "Bearer {}".format(api_key), 'Content-Type': 'application/json'},
                json=self.build_request_body(email)
                )
