from flask import Flask, render_template, request, abort
import sqlite3
import csv
import io
import json

app = Flask(__name__)

# Exemple de données en JSON
products_json = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]

def get_products_from_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        # Convertir en liste de dict
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        return products
    except Exception as e:
        print(f"Database error: {e}")
        return None

def get_products_from_csv():
    # Créer un CSV en mémoire à partir de la liste JSON (exemple)
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["id", "name", "category", "price"])
    writer.writeheader()
    for product in products_json:
        writer.writerow(product)
    output.seek(0)
    # Convertir CSV en liste de dict (juste pour l'exemple)
    products = []
    reader = csv.DictReader(output)
    for row in reader:
        # Convertir types
        products.append({
            "id": int(row["id"]),
            "name": row["name"],
            "category": row["category"],
            "price": float(row["price"])
        })
    return products

@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()

    if source == 'json':
        products = products_json
    elif source == 'csv':
        products = get_products_from_csv()
    elif source == 'sql':
        products = get_products_from_db()
        if products is None:
            return "Database error occurred", 500
    else:
        return "Wrong source", 400

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
