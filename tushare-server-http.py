from flask import Flask
import tushare as ts

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/get_money_supply")
def get_money_supply():
    df = ts.get_money_supply()
    return df.to_json(orient='split')


@app.route("/get_today_all")
def get_today_all():
    df = ts.get_today_all()
    return df.to_json(orient='split')

@app.route("/get_stock_basics")
def get_stock_basics():
    df = ts.get_stock_basics()
    return df.to_json(orient='split')

app.run()