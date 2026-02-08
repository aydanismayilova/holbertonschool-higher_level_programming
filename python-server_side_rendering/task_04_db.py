#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def load_from_json():
    with open("products.json", "r") as f:
        return json.load(f)


def load_from_csv():
    products = []
    with open("products.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


def load_from_sql():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    products = []
    error = None

    try:
        if source == "json":
            products = load_from_json()
        elif source == "csv":
            products = load_from_csv()
        elif source == "sql":
            products = load_from_sql()
        else:
            error = "Wrong source"
            return render_template("product_display.html", error=error)
    except Exception:
        error = "Database error"
        return render_template("product_display.html", error=error)

    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Product not found"

    return render_template(
        "product_display.html",
        products=products,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
