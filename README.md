# 🛒 ShopHub — E-Commerce Backend API

ShopHub is a backend-focused E-Commerce REST API built with **Python, Django, and Django REST Framework**.

The application provides APIs for authentication, product and category management, cart, wishlist, address management, order processing, inventory management, and Razorpay payment integration.

The project uses **PostgreSQL** for persistent data storage, **JWT authentication** for secured APIs, and **role-based access control** for customer and administrator operations.

The application is deployed on **Render** and the payment workflow has been tested using Razorpay Test Mode.

---

## 🚀 Features

### 🔐 Authentication & Authorization

- User registration
- User login
- JWT-based authentication
- Access and refresh tokens
- Protected API endpoints
- User-specific resources
- Role-based access control
- Admin-only management operations

### 👥 User Roles

#### Customer

Customers can:

- Browse products
- View categories
- Search and filter products
- Manage cart
- Manage wishlist
- Manage addresses
- Checkout products
- Make payments
- View their own orders
- View order details
- Cancel eligible orders

#### Administrator

Administrators can:

- Create products
- Update products
- Delete products
- Create categories
- Update categories
- Delete categories
- Manage order status
- Access Django Admin Panel

Admin-only APIs are protected using Django REST Framework's permission system.

---

## 📦 Product Management

- Product CRUD APIs
- Category-based products
- Product search
- Brand filtering
- Price range filtering
- Pagination
- Product image support
- Admin-only product creation
- Admin-only product updates
- Admin-only product deletion

---

## 🗂️ Category Management

- Category listing
- Category detail
- Category creation
- Category updates
- Category deletion
- Admin-only category management

---

## 🛒 Cart Management

- Add products to cart
- Update product quantity
- Remove products from cart
- View authenticated user's cart
- User-specific cart data

---

## ❤️ Wishlist

- Add products to wishlist
- Remove products from wishlist
- View authenticated user's wishlist
- User-specific wishlist data

---

## 📍 Address Management

- Create address
- View saved addresses
- Update address
- Partial address updates
- Delete address
- Set default address
- Automatically assign the first address as default
- User-specific address data

---

## 📋 Order Management

- Checkout API
- Order creation
- Order item management
- Order address snapshot
- Order list API
- Order detail API
- Order status tracking
- Order cancellation
- Admin order status management
- Payment status tracking
- Stock validation during checkout
- Inventory update after successful payment
- Order confirmation after successful payment

---

## 💳 Razorpay Payment Integration

ShopHub integrates Razorpay for payment processing.

### Payment Flow

- Create Razorpay order
- Open Razorpay Checkout
- Process payment
- Receive payment response
- Verify Razorpay payment signature
- Update payment status
- Confirm order
- Reduce product stock
- Clear cart after successful payment

Razorpay Test Mode is used for development and demonstration.

---

## 🔒 Security

- JWT authentication
- Protected APIs
- Role-based access control
- Admin-only product management
- Admin-only category management
- Admin-only order status updates
- User-specific resource access
- Environment variables for sensitive configuration
- Razorpay secret kept on the backend
- Server-side Razorpay signature verification
- `.env` excluded from Git
- Database credentials excluded from source code

---

## 🗄️ Database

ShopHub uses **PostgreSQL** as the primary database.

Implemented using:

- Django ORM
- Django migrations
- Foreign key relationships
- Environment-based database configuration
- Database transactions for checkout operations

---

## 🧪 Testing

The project includes automated API tests covering important authentication, authorization, and order-related scenarios.

Current test result:

```text
Ran 4 tests
OK

🏗️ Backend Architecture
Client
   │
   ▼
Django REST Framework APIs
   │
   ▼
Authentication & Permissions
   │
   ▼
Serializers
   │
   ▼
Django ORM
   │
   ▼
PostgreSQL

Payment Architecture
Client
   │
   │ Checkout Request
   ▼
Django Backend
   │
   ├── Validate Cart
   ├── Validate Stock
   ├── Create ShopHub Order
   ├── Create Order Items
   └── Create Razorpay Order
           │
           ▼
       Razorpay
           │
           │ Payment
           ▼
        Client
           │
           │ Payment Response
           ▼
   Payment Verification API
           │
           ▼
   Verify Razorpay Signature
           │
           ▼
   Payment Status = Completed
           │
           ▼
   Order Status = Confirmed
           │
           ├── Reduce Stock
           │
           └── Clear Cart

Application Flow 
User Registration
       ↓
User Login
       ↓
JWT Access Token
       ↓
Browse Products
       ↓
Search / Filter / Pagination
       ↓
Add Product to Cart
       ↓
Manage Cart
       ↓
Add Products to Wishlist
       ↓
Create Address
       ↓
Checkout
       ↓
Stock Validation
       ↓
Create Order
       ↓
Create Razorpay Order
       ↓
Razorpay Checkout
       ↓
Complete Payment
       ↓
Verify Razorpay Signature
       ↓
Payment Completed
       ↓
Order Confirmed
       ↓
Inventory Updated
       ↓
Cart Cleared

🛠️ Tech Stack
Technology	                       Purpose
Python	                         Backend programming
Django	                         Web framework
Django REST Framework	         REST API development
PostgreSQL	                     Relational database
JWT / SimpleJWT	                 Authentication
Razorpay	                     Payment gateway
django-cors-headers	             CORS handling
Postman	                         API testing
Gunicorn	                     Application server
WhiteNoise	                     Static file serving
Render	                         Deployment
Git	                             Version control
GitHub                         	 Source code hosting

🏗️ Project Structure
ShopHub/
│
├── accounts/
│
├── addresses/
│
├── cart/
│
├── categories/
│
├── orders/
│
├── payments/
│
├── products/
│
├── wishlist/
│
├── shophub/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── templates/
│   └── payment.html
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/Jaswanthroyg/shophub.git
cd shophub
2. Create a virtual environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
🐘 PostgreSQL Configuration

Create a PostgreSQL database and configure the database connection using environment variables.

Example:

DB_NAME=your_database_name
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_HOST=localhost
DB_PORT=5432
🔑 Environment Variables

Create a .env file in the project root:

SECRET_KEY=your_django_secret_key

DEBUG=True

DB_NAME=your_database_name
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_HOST=localhost
DB_PORT=5432

RAZORPAY_KEY_ID=your_razorpay_test_key_id
RAZORPAY_KEY_SECRET=your_razorpay_test_key_secret

Never commit .env or real credentials to GitHub.

🗃️ Database Migrations

Create migrations when models are changed:

python manage.py makemigrations

Apply migrations:

python manage.py migrate
▶️ Run the Development Server
python manage.py runserver

Local backend:

http://127.0.0.1:8000/

Payment page:

http://127.0.0.1:8000/payment/

👨‍💻 Author

Jaswanth Roy Gorre

Backend Developer | Python | Django | Django REST Framework

GitHub

https://github.com/Jaswanthroyg

⭐ ShopHub

ShopHub is a backend-focused E-Commerce REST API demonstrating practical backend development with Django REST Framework, PostgreSQL, JWT authentication, role-based access control, inventory management, and Razorpay payment integration and deployed on Render.