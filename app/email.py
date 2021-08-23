from html2text import html2text

class Email:
    def __init__(self, request_body):
        self.to_email = request_body['to']
        self.to_name = request_body['to_name']
        self.from_email = request_body['from']
        self.from_name = request_body['from_name']
        self.subject = request_body['subject']
        self.body = html2text(request_body['body'])
