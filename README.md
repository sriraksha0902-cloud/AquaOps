# AquaOps – Business Analytics & Secure Data Management System

AquaOps is a business analytics and data management system developed for a water-tech startup. The system connects a MySQL database with a Flask backend and a web-based dashboard to provide business insights while incorporating basic application security and audit logging.

## 🚀 Features

### Business Analytics
- Real-time calculation of total revenue
- Total expense tracking
- Automatic profit calculation
- Data retrieved directly from MySQL
- Web-based analytics dashboard

### Database Management
- MySQL relational database
- Structured tables for:
  - Customers
  - Products
  - Sales Orders
  - Sales Items
  - Expenses
- Flask backend for database interaction

### 🔐 Security Features
- Database credentials stored using environment variables
- `.env` excluded from version control using `.gitignore`
- Separate database user for application access
- Application audit logging
- Records HTTP requests and responses
- Records request timestamps
- Records client IP addresses
- Records HTTP response status codes

## 🏗️ System Architecture

The system follows a simple three-layer architecture:

Frontend  
↓  
Flask REST API  
↓  
MySQL Database

The frontend communicates with the Flask backend through HTTP requests. The backend retrieves and processes data from MySQL and returns the results to the dashboard.

## 🛠️ Technologies Used

- Python
- Flask
- Flask-CORS
- MySQL
- MySQL Connector/Python
- HTML
- JavaScript
- CSS
- python-dotenv
- Git/GitHub

## 📁 Project Structure

```text
AquaOps/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   └── analytics.py
│
├── database/
│
├── docs/
│
├── frontend/
│   └── index.html
│
├── screenshots/
│
├── .env
├── .gitignore
├── LICENSE
└── README.md