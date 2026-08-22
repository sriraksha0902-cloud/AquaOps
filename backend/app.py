from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from db import get_connection
import logging
from datetime import datetime

app = Flask(__name__)
CORS(app)
logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.before_request
def log_request():
    logging.info(
        f"REQUEST: {request.method} {request.path} from {request.remote_addr}"
    )

@app.after_request
def log_response(response):
    logging.info(
        f"RESPONSE: {request.method} {request.path} - STATUS {response.status_code}"
    )
    return response
import os
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")
@app.route("/analytics/profit", methods=["GET"])
def profit():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COALESCE(SUM(total_amount), 0) FROM sales_orders")
    revenue = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses")
    expenses = cursor.fetchone()[0]

    profit_value = revenue - expenses

    cursor.close()
    conn.close()

    return jsonify({
        "total_revenue": float(revenue),
        "total_expenses": float(expenses),
        "profit": float(profit_value)
    })


if __name__ == "__main__":
    app.run(debug=True)