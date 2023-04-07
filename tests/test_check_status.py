import pytest
from application import app

# documentation link - I don't understand everything but I am going to give it a try
# https://flask.palletsprojects.com/en/2.2.x/testing/
# Here I am trying to write a test to check the status code of our pages on loading - looking to see if all the links work

@pytest.fixture
def client():
    app.config['TESTING'] = True
    print(app.config)
    return app.test_client()

def test_request_index(client):
    response = client.get("/")
    assert b"<h1>Welcome to ChipIn, the best personal finance tool in the UK.</h1>" in response.data

def test_request_dashboard(client):
    response = client.get("/dashboard")
    assert b"<h1>Dashboard</h1>" in response.data

