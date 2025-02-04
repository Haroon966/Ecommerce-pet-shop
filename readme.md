# Ecommerce Store Project

Welcome to the **Ecommerce Store Project**! This is a simple yet powerful eCommerce application built using **Django**, a Python web framework. The project enables users to browse products, add items to their cart, and manage their shopping experience with ease.

---

## 🚀 Features
- 🛒 **Product Listings** – Browse and view available products.
- ➕ **Add to Cart** – Seamlessly add products to your cart.
- 🛍 **Shopping Cart** – View and manage items before checkout.
- 👤 **User Authentication** – Sign up, log in, and log out.
- ⚙️ **Admin Panel** – Manage products and orders.

---

## 📂 Project Structure
The project is organized as follows:

```
Ecommerce-Pet-Shop/
│── ecommerce/               # Main project directory
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│── store/                   # Main application
│   ├── views.py             # Views handling requests
│   ├── models.py            # Database models
│   ├── forms.py             # Forms for user input
│   ├── urls.py              # URL patterns for store app
│   ├── templates/store/     # HTML templates
│── db.sqlite3               # SQLite database
│── manage.py                # Django management script
│── requirements.txt         # List of dependencies
│── README.md                # Project documentation
```

---

## 🎯 How It Works
### **1️⃣ Product Listings**
Displays a catalog of available products, retrieved from the database.

### **2️⃣ Add to Cart**
Allows users to add items to their cart, storing them in the session.

### **3️⃣ View Cart**
Displays all products added to the cart along with quantities.

### **4️⃣ User Authentication**
Users can **sign up, log in, and log out** to manage their purchases.

---

## 🎨 Templates
The project includes the following templates for a smooth user experience:

- `product_list.html` – Displays all products.
- `add_product.html` – Allows users to add items.
- `cart.html` – Shows items in the cart.
- `signup.html` – User registration page.

---

## 🗂 Models
The application consists of:

- **Product Model** – Represents each product in the store.
- **Order Model** – Tracks user purchases and orders.

---

## 🌍 URL Patterns
- `/` – Product listings page.
- `/cart/` – View the shopping cart.
- `/add-to-cart/<int:product_id>/` – Add a product to the cart.
- `/signup/` – User registration page.
- `/logout/` – Logs out the user.

---

## 🔧 Installation Guide
### **Prerequisites**
Ensure you have **Python** and **Django** installed.

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/Ecommerce-Pet-Shop.git
cd Ecommerce-Pet-Shop
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run Migrations**
```sh
python manage.py migrate
```

### **4️⃣ Start the Development Server**
```sh
python manage.py runserver
```

### **5️⃣ Open the Application**
Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 💡 Contributing
Want to improve this project? Contributions are welcome!

1. Fork the repository 📌
2. Create a new branch (`git checkout -b feature-branch`) 🛠
3. Commit your changes (`git commit -m 'Added new feature'`) ✅
4. Push to your branch (`git push origin feature-branch`) 🚀
5. Create a Pull Request! 🎉

---

## 📞 Contact
For any inquiries, feel free to reach out:
📧 Email: **haroondev9@gmail.com**
📌 GitHub: [Haroon966](https://github.com/Haroon966))

Happy Coding! 🎉🐾
