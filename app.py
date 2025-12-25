# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import db # Import your existing database module

app = Flask(__name__)
# Enable CORS for all routes, allowing your frontend to access the API
CORS(app) 

# --- API Endpoints ---

# 1. Add Category (POST)
@app.route('/api/add_category', methods=['POST'])
def add_category_api():
    try:
        data = request.get_json()
        name = data.get('name')
        
        if not name:
            return jsonify({"status": "error", "message": "Category name cannot be empty."}), 400
        
        db.add_category(name)
        return jsonify({"status": "success", "message": f"Category '{name}' added."}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 2. Get Categories (GET)
@app.route('/api/categories', methods=['GET'])
def get_categories_api():
    try:
        categories = db.get_categories()
        # Convert the list of tuples [(1, 'Food'), (2, 'Travel')] to a list of objects for JSON
        categories_list = [{"id": cat_id, "name": cat_name} for cat_id, cat_name in categories]
        return jsonify(categories_list), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 3. Add Expense (POST)
@app.route('/api/add_expense', methods=['POST'])
def add_expense_api():
    try:
        data = request.get_json()
        category_id = int(data.get('category_id'))
        description = data.get('description')
        amount = float(data.get('amount'))
        date_str = data.get('expense_date')

        # Handle date parsing, defaulting to today if empty/missing
        expense_date = datetime.now().date()
        if date_str:
             expense_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        db.add_expense(category_id, description, amount, expense_date)
        return jsonify({"status": "success", "message": "Expense added successfully."}), 201
    except ValueError:
        return jsonify({"status": "error", "message": "Invalid input for category ID or amount."}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 4. Get Expenses (GET)
@app.route('/api/expenses', methods=['GET'])
def get_expenses_api():
    try:
        expenses = db.get_expenses()
        expenses_list = [{
            "id": exp_id, 
            "category": cat_name, 
            "description": desc, 
            "amount": amount, 
            "date": date.strftime('%Y-%m-%d')
        } for exp_id, cat_name, desc, amount, date in expenses]
        return jsonify(expenses_list), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 5. Get Summary (GET)
@app.route('/api/summary', methods=['GET'])
def get_summary_api():
    try:
        summary = db.get_summary()
        summary_list = [{"category": cat_name, "total": total} for cat_name, total in summary]
        return jsonify(summary_list), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 6. Delete Category (DELETE)
@app.route('/api/delete_category/<int:category_id>', methods=['DELETE'])
def delete_category_api(category_id):
    try:
        # Check if the category exists (optional, but good practice)
        categories = db.get_categories()
        if category_id not in [cat[0] for cat in categories]:
             return jsonify({"status": "error", "message": "Invalid category ID."}), 404
             
        # Execute the deletion logic (deleting expenses first, then category)
        db.delete_expenses_by_category(category_id)
        db.delete_category(category_id)
        return jsonify({"status": "success", "message": f"Category ID {category_id} and associated expenses deleted."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    # You can change the port if needed
    app.run(debug=True, port=5000)