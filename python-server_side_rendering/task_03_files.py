from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

@app.route('/items')
def items():
    """
    Read items from a JSON file and render the items page.
    If the file is missing or corrupted, return an empty list.
    """
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        items = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        # Handle missing or invalid JSON file gracefully
        items = []
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    """
    Handle the /products route.
    Reads products from either JSON or CSV files based on the 'source' query parameter.
    Optionally filters products by 'id' query parameter.
    Renders the product_display.html template with the results or error messages.
    """
    source = request.args.get('source')  # Get the data source: 'json' or 'csv'
    id_param = request.args.get('id')    # Optional product ID filter
    error = None
    products = []

    # Load products from the specified source
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except Exception:
            error = "Could not read JSON file."
    elif source == 'csv':
        try:
            with open('products.csv', 'r', newline='') as f:
                reader = csv.DictReader(f)
                products = []
                for row in reader:
                    # Convert fields to appropriate types
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products.append(row)
        except Exception:
            error = "Could not read CSV file."
    else:
        error = "Wrong source"

    # Filter by product ID if provided and no previous error
    if id_param and not error:
        try:
            id_int = int(id_param)
            filtered = [p for p in products if p['id'] == id_int]
            if filtered:
                products = filtered
            else:
                error = "Product not found"
                products = []
        except Exception:
            error = "Invalid ID"
            products = []

    # Render the template with either products or an error message
    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
