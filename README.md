# 🌸 Flowerista - Online Flower Shop

**Flowerista** is a full-featured e-commerce web application built from scratch to bring fresh, handcrafted flower bouquets to customers all across Egypt. The platform features catalog browsing, seamless shopping cart management, user authentication, and order fulfillment integrated with **Bosta Delivery Services**.

---

## ✨ Features

- **Flower Catalog & Store:** Browse custom-designed flower bouquets categorized by occasion, arrangement style, and price.
- **Dynamic Shopping Cart & Checkout:** Add, modify, and review items before placing orders.
- **Bosta Shipping Integration:** Seamless delivery management and shipment tracking across all governorates in Egypt via Bosta.
- **User Authentication:** Account creation, login, order history, and personal delivery address management.
- **Admin Management:** Custom Django backend for managing catalog products, tracking orders, and handling fulfillment.

---

## 🛠️ Tech Stack & Dependencies

- **Backend:** Python, Django
- **Database:** SQLite (`db.sqlite3`)
- **Frontend:** HTML5, CSS3, JavaScript (Static assets)
- **Logistics & Shipping:** Bosta API Integration

---

## 📂 Project Structure

```text
Flowerista/
│
├── flowerista/            # Core Django project settings and root configuration
├── store/                 # Main e-commerce app (models, views, cart, checkout)
├── static/                # CSS, JavaScript, and static image assets
├── templates/             # HTML templates for store pages
├── venv/                  # Python Virtual Environment (ignored by Git)
│
├── .gitignore             # Git ignore configuration
├── db.sqlite3             # Local SQLite database
├── manage.py              # Django CLI management script
├── models.py              # Application database models
├── urls.py                # Global URL routing
├── views.py               # Application views & request handling
├── package.json           # Frontend package dependencies
└── README.md


git clone [https://github.com/leo977-byte/flowerista.git](https://github.com/leo977-byte/flowerista.git)
cd flowerista
# Create virtual environment
python -m venv venv

# Activate on Windows (Git Bash / CMD)
source venv/Scripts/activate   # Git Bash
# OR
venv\Scripts\activate          # CMD
pip install django requests
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
