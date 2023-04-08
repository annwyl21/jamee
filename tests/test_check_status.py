import pytest
from application import app

# type this in your terminal to see the tests passing
# python -m pytest

# documentation link - I don't understand everything but I am going to give it a try
# https://flask.palletsprojects.com/en/2.2.x/testing/

# I think this starts the app in the background in a 'testing' mode
@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

# This is pytest looking for some text in each page when the page has loaded.
# index page - an information page
def test_request_index(client):
    response = client.get("/")
    assert b"<h1>Welcome to ChipIn, the best personal finance tool in the UK.</h1>" in response.data

# dashboard page - a page with elements that generate using database queries that might fail
def test_request_dashboard(client):
    response = client.get("/dashboard")
    assert b"<h1>Dashboard</h1>" in response.data

# articles/ benefits template page - a page where the text changes depending on which route was selected
# and different text is selected from the database for each page
def test_request_benefits(client):
    response = client.get("/child-benefit")
    assert b"You get Child Benefit if you are responsible for bringing up a child" in response.data

