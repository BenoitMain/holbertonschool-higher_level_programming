from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
    try:
        filename = "items.json"
        with  open(filename, "r") as f:
            data = json.load(f)
        items_list = data["items"]
        return render_template("items.html", items=items_list)
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return render_template("items.html", items=[])

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    products = []

    if source == "json":
        try:
            with open("products.json", "r") as f:
                data = json.load(f)
            products = data
        except Exception:
            error = "Could not read JSON file."

    elif source == "csv":
        try:
            with open("products.csv", "r") as f:
                reader = csv.DictReader(f)
                products = []
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products.append(row)
        except Exception:
            error = "Could not read CSV file."

    elif source == "sql":
        try:
            products = get_products_from_sqlite(id_param)
            if id_param and not products:
                error = "Product not found"
        except Exception as e:
            error = f"Database error: {e}"
            products = []

    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)

    if id_param and not error:
        try:
            search_id = int(id_param)
            filtered = [p for p in products if int(p['id']) == search_id]
            if filtered:
                products = filtered
            else:
                error = "Product not found"
                products = []
        except Exception:
            error = "Invalid id"
            products = []

    return render_template("product_display.html", products=products, error=error)

def get_products_from_sqlite(id_param=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    if id_param:
        cursor.execute('SELECT id, name, category, price FROM Products WHERE id=?', (id_param,))
    else:
        cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    conn.close()
    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
