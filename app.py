from flask import Flask, render_template, request
import requests
  
def get_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    return data[0]["rates"]

app = Flask(__name__)

@app.route("/calculator", methods=["GET", "POST"])
def currency_calculator():
    if request.method == "POST":

            amount = request.form['amount']
            amount = float(amount)
            currency = request.form['currency']
            rates = get_rates()

            for i in rates:
                if currency == i['code']:
                    rate = i['ask']
                    currency_name = i['currency'] 

            rate = float(rate)
            result = rate * amount
            return render_template ("currencies.html", result=round(result, 2), amount=amount, currency=currency ,currency_name=currency_name)
    
    
    else:
        return render_template("currencies.html")


if __name__ == "__main__":
    app.run(debug=True)
