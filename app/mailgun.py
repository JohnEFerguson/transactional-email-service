import requests

class MailgunClient:

    _base_url = "https://api.mailgun.net/v3/sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org/messages"

    def build_request_body(self, email):
        return {
                "from": "{} <{}>".format(email.from_name, email.from_email),
                "to": [email.to_email],
                "subject": email.subject,
                "text": email.body
                }


    def send_via_mailgun(self, email, api_key):
        return requests.post(
                self._base_url,
                auth=("api", api_key), 
                data=self.build_request_body(email)
                )
