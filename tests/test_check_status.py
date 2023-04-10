import pytest
from application import app
from application.finance import Finance

# type this in your terminal to see the tests passing
# python -m pytest

# documentation link - I don't understand everything but I am going to give it a try
# https://flask.palletsprojects.com/en/2.2.x/testing/

# I think this starts the app in the background in a 'testing' mode
@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

# BDD: GIVEN, WHEN, THEN

# TESTING THE HOME PAGE
# GIVEN I have entered localhost:5000/ to request the home page
def test_request_index(client):
# WHEN I 'GET' the page
    response = client.get("/")
# THEN the following text should load at the end of the page
    assert b"<h3>Why ChipIn?</h3>" in response.data

# TESTING THE DASHBOARD PAGE - a page with elements that generate using database queries that might fail
# GIVEN I have entered my monthly spending on the form page
def test_request_dashboard(client):
# WHEN I click submit
    response = client.get("/dashboard")
# THEN the dashboard page should load and I should see 2 graphs and 3 tables
# This test is checking to see that the last of those 5 elements has loaded
    assert b"<h2>Your annual spending</h2>" in response.data



# TESTING THE DASHBOARD PAGE WEEKLY CALCULATOR
# GIVEN I have entered my monthly spending on rent as 1k on the form page
def test_dashboard_weekly_calculator():
# WHEN I click submit
    test_list = [1000, 0, 0, 0, 0, 0, 0, 0, 0]
    results = Finance('test').dashboard_weekly_calculator(test_list)
# THEN my weekly rent spending should be calculated as £231
    assert results == [231, 0, 0, 0, 0, 0, 0, 0, 0], "Dashboard Weekly Calculator Incorrect"



# TESTING THE DASHBOARD ANNUAL CALCULATOR
# GIVEN I have entered my monthly spending on rent as 1k on the form page
@pytest.mark.parametrize("test_list", [
        ([1000, 0, 0, 0, 0, 0, 0, 0, 0]),
        ([-1000, 0, 0, 0, 0, 0, 0, 0, 0])
    ])
def test_dashboard_annual_calculator(test_list):
# WHEN I click submit
    results = Finance('test').dashboard_annual_calculator(test_list)
# THEN my annual rent spending should be calculated as 12k
    assert results[0] == 12000, f"Dashboard Annual Calculator Incorrect: {results[0]}"



# TESTING THE BENEFITS TEMPLATE - a page where different text is selected from the database depending on which route was selected
# GIVEN a selection of benefits to click on the nav bar
def test_request_benefits(client):
# WHEN I click on the Child Benefit option
    response = client.get("/child-benefit")
# THEN I chould see a webpage that displays information about specifically child benefit
    assert b"You get Child Benefit if you are responsible for bringing up a child" in response.data


# GIVEN a simple debt calculator
def test_simple_debt_calc():
# WHEN I enter my debt amount of 10K, my interest rate of 5% and the loan period of 5 years 
    information = [10000, 5, 5, 'years']
    results = Finance('test').simple_debt_calculator(information)
# THEN the calculator should show me that the total cost of my loan over 12 years will be 12.5K
    assert results == 12500, "Simple Debt Calculator Incorrect"
    

