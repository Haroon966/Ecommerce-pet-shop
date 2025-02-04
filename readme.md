## README.md

Ecommerce Store Project
This is a simple ecommerce store project built using Django, a Python web framework. The project allows users to view products, add products to cart, and view their cart.

Project Structure
The project is structured as follows:

store: This is the main app directory.
store/views.py: This file contains the views for the project, including the product list view, add to cart view, view cart view, signup view, and logout view.
store/templates/store: This directory contains the HTML templates for the project, including the product list template, add product template, cart template, and signup template.
store/models.py: This file contains the models for the project, including the Product model and Order model.
store/forms.py: This file contains the forms for the project, including the ProductForm.
store/urls.py: This file contains the URL patterns for the project.
ecommerce: This is the project directory.
ecommerce/settings.py: This file contains the project settings.
ecommerce/urls.py: This file contains the URL patterns for the project.
How it Works
Here's a step-by-step explanation of how the project works:

Product List View: The product list view displays a list of all products in the database. The view uses the Product model to retrieve the products and the product_list.html template to display them.
Add to Cart View: The add to cart view allows users to add products to their cart. The view uses the Product model to retrieve the product and the cart session variable to store the product ID and quantity.
View Cart View: The view cart view displays the products in the user's cart. The view uses the cart session variable to retrieve the product IDs and quantities, and the Product model to retrieve the product details.
Signup View: The signup view allows users to create an account. The view uses the User CreationForm to validate the user's input and create a new user account.
Logout View: The logout view logs the user out of their account.
Templates
The project uses the following templates:

product_list.html: This template displays the product list.
add_product.html: This template allows users to add products to their cart.
cart.html: This template displays the products in the user's cart.
signup.html: This template allows users to create an account.
Models
The project uses the following models:

Product: This model represents a product in the database.
Order: This model represents an order in the database.
Forms
The project uses the following forms:

ProductForm: This form validates the product data and creates a new product instance.
URL Patterns
The project uses the following URL patterns:

/: This URL pattern maps to the product list view.
/cart/: This URL pattern maps to the view cart view.
/add-to-cart/<int:product_id>/: This URL pattern maps to the add to cart view.
/signup/: This URL pattern maps to the signup view.
/logout/: This URL pattern maps to the logout view.
Requirements
The project requires the following dependencies:

Django
Python
Installation
To install the project, follow these steps:

Clone the repository using git clone.
Install the dependencies using pip install -r requirements.txt.
Run the migrations using python manage.py migrate.
Run the development server using python manage.py runserver.
Usage
To use the project, follow these steps:

Open a web browser and navigate to http://localhost:8000/.
View the product list by clicking on the "Products" link.
Add a product to your cart by clicking on the "Add to Cart" button.
View your cart by clicking on the "Cart" link.
Create an account by clicking on the "Signup" link.
Logout of your account by clicking on the "Logout" link.
