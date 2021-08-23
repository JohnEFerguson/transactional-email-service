# Transactional Email Service

## Install
Using Python3
- Use pip or anaconda to install the packages in requirements.txt
- Fill in the required api keys in .env
## Run
### Using Mailgun
```
    $ FLASK_APP=app FLASK_ENV=production API_TO_USE=mailgun flask run
```
### Using Sendgrid
```
    $ FLASK_APP=app FLASK_ENV=production API_TO_USE=sendgrid flask run
```

## Test
### Unit testing
```
    $ python3 -m pytest -v 
```
### Integration testing
- Run the app for Mailgun
- Run from the commandline:
```
curl -d '{
"to": "john.everett.ferguson@gmail.com",
"to_name": "Mr. Fake",
"from": "mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org",
"from_name":"Ms. Fake",
"subject": "A message from The Fake Family",
"body": "<h1>Your Bill</h1><p>$10</p>"
}' -H "Content-Type: application/json" -X POST http://localhost:5000/email
```
- Run the app for Sendgrid
- Run from the commandline:
```
curl -d '{
"to": "john.everett.ferguson@gmail.com",
"to_name": "Mr. Fake",
"from": "john.everett.ferguson@gmail.com",                            
"from_name":"Ms. Fake",
"subject": "A message from The Fake Family", 
"body": "<h1>Your Bill</h1><p>$10</p>"
}' -H "Content-Type: application/json" -X POST http://localhost:5000/email
```
## Discussion

This task took ~6 hours
### Technical Choices

This app is built using Python3 and Flask. The advantages of using Python for a task like this are 
- Not a lot of code required to bootstrap
- Quick iteration
- Accessible libraries for doing the simple data processing required

Similarly, Flask offers
- Lightweight, quick iteration
    - tradeoff: when the app gets more complicated, organizing code in the project becomes difficult with so much flexibility
- Lots of open-source tools, examples, templates

### Next steps
- Default behavior could be: Try with mailgun, retry with sendgrid in case of failures 
- More unit test coverage
- Logging
- More specific exception handling
- Separate into controllers, services, and data models
- Authenticate requests
- Deployment details like server url, port, etc should be configurable
- Containerize and use DevOps tools like Ansible, Kubernetes for deployment
- Use a production-ready server, not wsgi
- Write integration tests which cover functionality of Mailgun and Sendgrid
- Add a datalayer to keep track of requests to avoid duplicates

