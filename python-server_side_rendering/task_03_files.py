from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to read JSON data
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to read CSV data
def read_csv(file_path):
    products = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert id and price to proper types
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
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
    else:
        error = "Wrong source"

    if not error and product_id is not None:
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            error = "Product not found"

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
