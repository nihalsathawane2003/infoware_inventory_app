# Infoware Inventory App

A desktop inventory and sales application built using **PySide6** and **MySQL**.

---

## 📦 Features

- Admin & Operator login with secure bcrypt hashed passwords
- Product Master (barcode, GST, unit, image, etc.)
- Goods Receiving (adds to Inventory)
- Sales (deducts from Inventory)
- Inventory validations (min stock, max sales)

---

## 🛠️ Tech Stack

- Python 3.10+
- PySide6 (for GUI)
- MySQL
- bcrypt (password hashing)

---

## 🚀 Getting Started

### 1. Setup MySQL

```sql
CREATE DATABASE inventory_db;
```

### 2. Clone the Repo

```bash
git clone https://github.com/yourusername/infoware_inventory_app.git
cd infoware_inventory_app
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure DB

Update `db/db_config.py` with your local MySQL credentials.

### 5. Run the App

```bash
python main.py
```

### 6. Seed Sample Users

```bash
python seed_users.py
```

### ✔️ Sample Credentials

```
Username: operator1
Password: op1pass

Username: operator2
Password: op2pass
```

---

## 🔒 Security

- All passwords are hashed using `bcrypt`
- No plain-text password storage

---

## 🛠️ Build as EXE (Optional)

```bash
pip install pyinstaller
pyinstaller --noconfirm --windowed main.py
```

---

## 📹 Demo Video

Please check the accompanying demo video shared via drive/link.
