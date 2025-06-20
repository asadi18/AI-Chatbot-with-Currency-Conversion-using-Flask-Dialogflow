from flask import Flask, request,jsonify,render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    currencyToConvert = data['queryResult']['parameters']['unit-currency']['currency']
    currencyInConvert = data['queryResult']['parameters']['currency-name']
    url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_jB8itUK3cCcNrPvKjGT4i3NpZwdlhcCEJH8J8QAk&currencies=EUR%2CUSD%2CCAD%2CGBP'
    response = requests.get(url)
    usd = response.json()['data']['USD'] # we can use this api data as well but as this not worked we implemented manually bellow there was paid api options so, we are doing manually 2 currency to check the bot
    eur = response.json()['data']['EUR']
    
    
    if currencyToConvert == 'USD' and currencyInConvert == 'BDT':
        finalAmount = amount  * 122
        
    else: 
        finalAmount = amount * 140
        
        
    finalAmount = round(finalAmount, 2)
   
    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, currencyToConvert, currencyInConvert, finalAmount, currencyInConvert)}
    return jsonify(response)
    

if __name__ =="__main__": 
    app.run(debug=True)