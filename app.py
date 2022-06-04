from flask import Flask, render_template, request
import requests
  
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

for i in data:
    d = dict(i)

r =  d['rates']

for i in r:
    rates = list(r)

app = Flask(__name__)

@app.route("/calculator", methods=["GET", "POST"])
def currency_calculator():
    if request.method == "POST":

            amount = request.form['amount']
            amount = float(amount)
            currency = request.form['currency']

            if currency == 'USD': 
                rate = rates[0]['ask']
                currency_name = rates[0]['currency']
            if currency == 'AUD': 
                rate = rates[1]['ask']
                currency_name = rates[1]['currency']
            if currency == 'CAD': 
                rate = rates[2]['ask']
                currency_name = rates[2]['currency']
            if currency == 'EUR': 
                rate = rates[3]['ask']
                currency_name = rates[3]['currency']
            if currency == 'HUF': 
                rate = rates[4]['ask']
                currency_name = rates[4]['currency']
            if currency == 'CHF': 
                rate = rates[5]['ask']
                currency_name = rates[5]['currency']
            if currency == 'GBP': 
                rate = rates[6]['ask']
                currency_name = rates[6]['currency']
            if currency == 'JPY': 
                rate = rates[7]['ask']
                currency_name = rates[7]['currency']
            if currency == 'CZK': 
                rate = rates[8]['ask']
                currency_name = rates[8]['currency']
            if currency == 'DKK': 
                rate = rates[9]['ask']
                currency_name = rates[9]['currency']
            if currency == 'NOK': 
                rate = rates[10]['ask']
                currency_name = rates[10]['currency']
            if currency == 'SEK': 
                rate = rates[11]['ask']
                currency_name = rates[11]['currency']
            if currency == 'XDR': 
                rate = rates[12]['ask']
                currency_name = rates[12]['currency']

            rate = float(rate)
            result = rate * amount
            return render_template ("currencies.html", result=round(result, 2), amount=amount, currency=currency ,currency_name=currency_name)
    
    
    else:
        return render_template("currencies.html")


if __name__ == "__main__":
    app.run(debug=True)