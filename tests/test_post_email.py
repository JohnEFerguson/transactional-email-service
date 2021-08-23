def test_post_email_success(client):
    response = client.post("/email", 
            json={
                "to": "Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>",
                "to_name": "john.everett.ferguson@gmail.com",
                "from": "Hellooooo",
                "from_name": "Testing some Mailgun awesomness!",
                "subject": "Testing some Mailgun awesomness!",
                "body": "Testing some Mailgun awesomness!"
                }
            )
    assert response.status_code == 200

## maybe should not be allowed
def test_post_email_extra_param(client):
    response = client.post("/email", 
            json={
                "to": "Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>",
                "to_name": "john.everett.ferguson@gmail.com",
                "from": "Hellooooo",
                "from_name": "Testing some Mailgun awesomness!",
                "subject": "Testing some Mailgun awesomness!",
                "body": "Testing some Mailgun awesomness!",
                "boop": "bop"
                }
            )
    assert response.status_code == 200



def test_post_email_missing_param(client):
    response = client.post("/email", 
            json={
                "to": "Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>",
                "to_name": "john.everett.ferguson@gmail.com",
                "from": "Hellooooo",
                "from_name": "Testing some Mailgun awesomness!",
                "subject": "Testing some Mailgun awesomness!",
                }
            )
    assert response.status_code == 400 

def test_post_email_wrong_http_method(client):
    response = client.get("/email", 
            json={
                "to": "Excited User <mailgun@sandboxffc4573d4cd6461a953db1e213b31cea.mailgun.org>",
                "to_name": "john.everett.ferguson@gmail.com",
                "from": "Hellooooo",
                "from_name": "Testing some Mailgun awesomness!",
                "subject": "Testing some Mailgun awesomness!",
                }
            )
    assert response.status_code == 405 

