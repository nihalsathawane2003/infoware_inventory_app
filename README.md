# Infoware Inventory Management App

This is a desktop application built using Python and PySide6 for managing product inventory, sales, purchases, and user roles. It includes login functionality for Admin and Operator.

## Features

- Login system with user authentication
- Admin and Operator dashboards
- Add, view, and manage products
- Goods receiving with quantity, rate, GST, and total calculation
- Sales entry and inventory update
- View current inventory
- User role management (admin/operator)

## Technologies Used

- Python
- PySide6 (Qt for Python)
- MySQL (for storing data)
- hashlib (for password hashing)

## Folder Structure

- `ui/` - contains all UI-related Python files
- `db/` - database connection and query handling
- `utils/` - authentication and password hashing functions
- `main.py` - entry point of the application

## How to Run

1. Clone the repository  
2. Set up MySQL database using the provided SQL script  
3. Install required packages:  
   `pip install PySide6 mysql-connector-python`  
4. Run the application:  
   `python main.py`

## Author

Nihal Sathawane
