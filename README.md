# 🧠 Smart Inventory

A **Django-based Smart Inventory Management System** that helps businesses efficiently track, manage, and analyze their stock in real time. The app includes automated stock updates, smart notifications for low inventory, barcode/QR code integration, and insightful analytics dashboards.

---

## 🚀 Features

- 📦 **Product Management** – Add, update, and categorize products easily.  
- 🔔 **Low Stock Alerts** – Get automatic notifications when inventory is running low.  
- 📊 **Dashboard & Reports** – Visualize inventory trends, sales, and restock patterns.  
- 🧾 **Purchase & Sales Tracking** – Record supplier purchases and customer sales.  
- 🔍 **Search & Filters** – Quickly find items by name, SKU, or category.  
- 📱 **Responsive UI** – Fully functional on desktop and mobile devices.  
- 🧠 **Smart Analytics** – Predict inventory needs using historical data.  
- 🧾 **Barcode/QR Code Integration** *(optional)* – Scan products for quick entry and lookup.  

---

## 🏗️ Tech Stack

| Layer | Technology |
|:------|:------------|
| **Backend** | Django 5+, Python 3.11+ |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Database** | SQLite (dev) |
| **Auth** | Django’s built-in authentication system |
| **Other** | Django REST Framework (for APIs), Celery (optional for tasks) |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/smart-inventory.git
cd smart-inventory
```
### 2. Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Configure Environment Variables

Create a .env file in the project root:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```
### 5. Apply Migrations
```
python manage.py migrate
```
### 6. Create Superuser
``` 
python manage.py createsuperuser 
```
### 7. Run the Server
```
python manage.py runserver
```
Then open:
👉 http://127.0.0.1:8000/

## 🧰 Features to Extend
- Integration with barcode scanners
- Role-based access control (Admin, Staff, Viewer)
- REST API endpoints for mobile or IoT integration
- Auto-generated PDF invoices and reports
- Inventory forecasting with machine learning


## 💬 Contact
Author: Ali Asgor
📧 Email: hello@asgor.net
🌐 GitHub: @iamasgor