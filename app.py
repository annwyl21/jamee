from application import app

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

if __name__ == "__main__":
    app.run(debug=True)

# Assumptions
# There are no negative interest rates in our model - we do not yet account for them
# but this could be worth looking into in the future because they do exist in Sweden, Switzerland, Denmark and Japan
# https://www.investopedia.com/articles/investing/070915/how-negative-interest-rates-work.asp#:~:text=Negative%20interest%20rates%20are%20an,seemingly%20counterintuitive%2C%20monetary%20policy%20tool.&text=With%20negative%20interest%20rates%2C%20cash,rather%20than%20saving%20and%20hoarding.
