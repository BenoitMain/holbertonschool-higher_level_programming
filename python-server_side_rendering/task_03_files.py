from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    items = data.get('items', [])
    return render_template('items.html', items=items)

@app.route('/source')
def source():
    with open("products.json") as f:
        data = json.load(f)
    return data

@app.route('/products')
def products():
    source = request.args.get("source")
    id = request.args.get("id")
    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)
    return render_template("product_display.html", products=products)

def read_json():
    with open("products.json") as f:
        return json.load(f)

def read_csv():
    with open("products.csv", newline='') as f :
        reader = csv.DictReader(f)
        return list(reader)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
