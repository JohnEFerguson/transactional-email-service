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
```
    $ python3 -m pytest -v 
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
- Authenticate requests
- Deployment details like server url, port, etc should be configurable
- Containerize and use DevOps tools like Ansible, Kubernetes for deployment
- Use a production-ready server, not wsgi
- Write integration tests which cover functionality of Mailgun and Sendgrid
- Add a datalayer to keep track of requests to avoid duplicates

