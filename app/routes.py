from flask import render_template, redirect, url_for, request
from app.models import product

from app import app

@app.route("/")
@app.route("/<name>")
def hello(name='World'):
    return render_template("index.html", name=name)

@app.route("/extract")
def display_form():
    return render_template("extract.html")

@app.route("/extract", methods=['POST'])
def extract():
    product_id=request.form.get("product_id")
    product=product.Product(product_id)
    product.extract_reviews().extract_name().calculate_stats()
    product.export_reviews()
    product.export_info()
    return redirect(url_for('product', product_id=product_id))

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/product/<product_id>")
def product(product_id):
    return render_template("product.html", product_id=product_id)

@app.route("/charts/<product_id>")
def charts(product_id):
    return render_template("charts.html", product_id=product_id)

@app.route("/author")
def author():
    return render_template("author.html")

