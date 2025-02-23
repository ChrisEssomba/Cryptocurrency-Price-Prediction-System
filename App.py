 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import json


from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

# API Data Fetching Function
def get_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9841adaf-41fd-4102-8637-124871313e7a',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        results = data.get('data', [])
        
        df = pd.DataFrame(results)
        df = df.drop(columns=['tags', 'quote'])
        #df.to_csv('output.csv')
       #print(df)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e) 
    return df

# Flask Route for Home Page
@app.route("/")
def home():
    df = get_data()
    
    # Convert DataFrame to HTML Table
    table_html = df.to_html(classes="table table-striped", index=False)
    
    return render_template("index.html", table=table_html)

if __name__ == "__main__":
    app.run(debug=True)


