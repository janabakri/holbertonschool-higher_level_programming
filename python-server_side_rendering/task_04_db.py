from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Read JSON data
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Read CSV data
def read_csv(file_path):
    products = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# Read SQLite data
def read_sqlite(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error:
        return None
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products_list = []

    if source == 'json':
        try:
            products_list = read_json('products.json')
        except FileNotFoundError:
            error = "JSON file not found"
    elif source == 'csv':
        try:
            products_list = read_csv('products.csv')
        except FileNotFoundError:
            error = "CSV file not found"
    elif source == 'sql':
        products_list = read_sqlite('products.db')
        if products_list is None:
            error = "Database error"
    else:
        error = "Wrong source"

    if not error and product_id is not None:
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            error = "Product not found"

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
