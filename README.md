\# 🛒 ShopHub — E-Commerce Backend API

ShopHub is a backend-focused E-Commerce application built using Django and Django REST Framework.

The project provides REST APIs for user authentication, products, categories, cart, wishlist, address management, orders, and Razorpay payment processing.

The application uses PostgreSQL as the database and JWT authentication for protected APIs.


\## 🚀 Features

\### 🔐 Authentication

\- User registration

\- User login

\- JWT-based authentication

\- Protected APIs using authentication

\- User-specific resources


\### 📦 Products

\- Product APIs

\- Category-based products

\- Product filtering

\- Pagination

\- Product image support


\### 🗂️ Categories

\- Category management

\- Category image support

\- Products organized by categories


\### 🛒 Cart

\- Add products to cart

\- Update product quantity

\- Remove products from cart

\- View authenticated user's cart


\### ❤️ Wishlist

\- Add products to wishlist

\- Remove products from wishlist

\- View authenticated user's wishlist


\### 📍 Address Management

\- Create address

\- View saved addresses

\- Update address

\- Partial address updates

\- Delete address

\- Set default address

\- Automatically assign the first address as default


\### 📋 Orders

\- Checkout API

\- Order creation

\- Associate orders with addresses

\- Track order status

\- Track payment status

\- Confirm orders after successful payment


\### 💳 Razorpay Payment Integration

\- Razorpay Test Mode integration

\- Razorpay order creation

\- Razorpay Checkout

\- Payment processing

\- Razorpay signature verification

\- Payment status updates

\- Order confirmation after successful payment


\### 🗄️ Database

\- PostgreSQL

\- Django ORM

\- Django migrations

\- Environment-based database configuration


\### 🔒 Security

\- JWT authentication

\- Protected APIs

\- Environment variables for sensitive credentials

\- Razorpay secret kept on backend

\- Server-side payment signature verification

\- `.env` excluded from Git


\## 🛠️ Tech Stack

| Technology | Purpose |
---------------------------
| Python | Backend programming |

| Django | Web framework |

| Django REST Framework | REST API development |

| PostgreSQL | Database |

| JWT | Authentication |

| Razorpay | Payment Gateway |

| django-cors-headers | CORS handling |

| Postman | API testing |

| Git | Version control |

| GitHub | Source code hosting |

\---

\## 🏗️ Project Structure

ShopHub/

│

├── accounts/

├── addresses/

├── cart/

├── categories/

├── orders/

├── payments/

├── products/

├── wishlist/

│

├── shophub/

│   ├── settings.py

│   ├── urls.py

│   ├── wsgi.py

│   └── asgi.py

│

├── category\_images/

├── product\_images/

├── payment.html

├── manage.py

├── requirements.txt

├── .gitignore

└── README.md


🔄 Application Flow

User Registration

&#x20;      ↓

User Login

&#x20;      ↓

JWT Access Token

&#x20;      ↓

Browse Products

&#x20;      ↓

Filter / Paginate Products

&#x20;      ↓

Add Product to Cart

&#x20;      ↓

Manage Cart

&#x20;      ↓

Create Address

&#x20;      ↓

Checkout

&#x20;      ↓

Create Order

&#x20;      ↓

Create Razorpay Order

&#x20;      ↓

Razorpay Checkout

&#x20;      ↓

Complete Payment

&#x20;      ↓

Verify Razorpay Signature

&#x20;      ↓

Payment Completed

&#x20;      ↓

Order Confirmed

💳Payment Flow

Frontend

&#x20;  │

&#x20;  │ Checkout Request

&#x20;  ▼

Django Backend

&#x20;  │

&#x20;  ├── Create ShopHub Order

&#x20;  └── Create Razorpay Order

&#x20;          │

&#x20;          ▼

&#x20;      Razorpay

&#x20;          │

&#x20;          │ User Payment

&#x20;          ▼

&#x20;      Frontend

&#x20;          │

&#x20;          │ Payment Response

&#x20;          ▼

&#x20;  Payment Verification API

&#x20;          │

&#x20;          ▼

&#x20;  Verify Razorpay Signature

&#x20;          │

&#x20;          ▼

&#x20;  Payment Status = Completed

&#x20;          │

&#x20;          ▼

&#x20;  Order Status = Confirmed

\#Database:

python manage.py makemigrations

python manage.py migrate


⚙️Installation \& Setup

1\. Clone the repository

git clone https://github.com/Jaswanthroyg/shophub.git

cd shophub

2\. Create a virtual environment

Windows
python -m venv venv
venv\\Scripts\\Activate.ps1

Linux / macOS
python3 -m venv venv
source venv/bin/activate

3\. Install dependencies
pip install -r requirements.txt
🐘 PostgreSQL Configuration

Create a PostgreSQL database:
CREATE DATABASE backend\_journey;
Configure your PostgreSQL credentials using environment variables.

🔑Environment Variables

Create a .env file in the project root:
SECRET\_KEY=your\_django\_secret\_key

DEBUG=True

DB\_NAME=backend\_journey

DB\_USER=postgres

DB\_PASSWORD=your\_postgresql\_password

DB\_HOST=localhost

DB\_PORT=5432

RAZORPAY\_KEY\_ID=your\_razorpay\_test\_key\_id

RAZORPAY\_KEY\_SECRET=your\_razorpay\_test\_key\_secret

🗃️ Run Database Migrations

python manage.py migrate

▶️ Run the Development Server

python manage.py runserver

Backend:

http://127.0.0.1:8000/


🔐Authentication

ShopHub uses JWT authentication for protected APIs.
After login, send the access token in the request header:
Authorization: Bearer <access\_token>

📈 Future Improvements
Possible future improvements:
\-Automated unit and integration tests

\-Docker containerization

\-Production deployment

\-CI/CD pipeline

\-API documentation

\-Order history and tracking

\-Email notifications

\-Redis caching

\-Background task processing

\-Production Razorpay configuration

\-Dedicated production frontend

🧠 Backend Concepts Implemented
This project demonstrates:
\-REST API development

\-Django REST Framework

\-JWT authentication

\-Authentication \& permissions

\-Serializers

\-Django ORM

\-PostgreSQL integration

\-Database migrations

\-CRUD operations

\-Filtering

\-Pagination

\-User-specific data access

\-Database transactions

\-Payment gateway integration

\-Payment signature verification

\-Environment variable management

\-Git \& GitHub version control


👨‍💻 Author:
Jaswanth Roy Gorre
Backend Developer | Python | Django | Django REST Framework
GitHub:
https://github.com/Jaswanthroyg

⭐ ShopHub
A complete E-Commerce backend project demonstrating practical backend development with Django REST Framework, PostgreSQL, JWT authentication, and Razorpay payment integration.
\*\*One important point:\*\* don't put your actual `RAZORPAY\_KEY\_SECRET`, PostgreSQL password, JWT secret, or `.env` contents in this README. The placeholders are intentional.

