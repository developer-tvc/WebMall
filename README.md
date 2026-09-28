# WebMall

A Django-based e-commerce web application with a customer-facing shopping interface and a REST API backend. It supports product browsing, cart management, order placement, user authentication, and password management.

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Framework | Django 3.2 |
| REST API | Django REST Framework + Knox (Token Auth) |
| Task Queue | Celery + Redis |
| Database | SQLite (development) |
| Config | python-decouple |

## Features

### Customer-Facing
- **Product Browsing** — View all products, filter by category (Saree, Casual Shirt, Mobile, Laptop)
- **Product Detail** — View individual product pages with description, pricing, and images
- **Shopping Cart** — Add products to cart and manage quantities
- **Buy Now** — Direct purchase flow
- **Checkout** — Complete order with address selection
- **Order Tracking** — View order history with status (Accepted, Packed, On The Way, Delivered, Cancelled)
- **Search & Autosuggest** — Search products and get real-time suggestions
- **Mobile Filtering** — Browse products filtered by mobile category with dynamic data
- **Profile Management** — View and manage user profile
- **Address Management** — Add and manage delivery addresses across Indian states
- **Password Management** — Change password, reset password via email

### REST API
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/product/` | List all products |
| POST | `/api/register/` | User registration |
| POST | `/api/login/` | User login (returns token) |
| POST | `/api/logout/` | User logout |
| POST | `/api/logoutall/` | Logout from all sessions |
| POST | `/api/change-password/` | Change password (authenticated) |
| POST | `/api/password_reset/` | Request password reset |

Authentication is handled via **Knox token authentication**.

## Project Structure

```
WebMall/
├── WebMall/                  # Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URL configuration
│   ├── celery.py             # Celery configuration
│   ├── asgi.py / wsgi.py     # ASGI/WSGI entry points
│
├── customer/                 # Customer-facing app
│   ├── models.py             # Customer model (name, locality, city, zipcode, state)
│   ├── views.py              # Registration, login, profile, password views
│   ├── forms.py              # Custom authentication & password forms
│   ├── urls.py               # Customer URL routes
│   ├── admin.py              # Admin configuration
│   └── templates/app/        # HTML templates
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       ├── customer_registration.html
│       ├── profile.html
│       ├── address.html
│       ├── product_detail.html
│       ├── add_to_cart.html
│       ├── buy_now.html
│       ├── check_out.html
│       ├── orders.html
│       ├── search.html
│       ├── mobile.html
│       └── password_*.html   # Password change/reset templates
│
├── product/                  # Product & order management app
│   ├── models.py             # Product, Cart, OrderPlaced models
│   ├── views.py              # Product listing, cart, checkout, order views
│   ├── urls.py               # Product URL routes
│   ├── serializers.py        # DRF serializers
│   ├── helper.py             # Utility helpers
│   ├── task.py               # Celery tasks
│   └── admin.py              # Admin configuration
│
├── api/                      # REST API app
│   ├── models.py
│   ├── views.py              # API views (register, login, product list)
│   ├── serializers.py        # DRF serializers
│   ├── urls.py               # API URL routes
│   └── admin.py
│
├── templates/                # Global templates directory
├── static/                   # Static files (CSS, JS, images)
├── media/                    # User-uploaded media (product images)
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management script
└── README.md
```

## Database Models

### Product
| Field | Type | Description |
|-------|------|-------------|
| title | CharField(100) | Product name |
| selling_price | FloatField | Original price |
| discounted_price | FloatField | Discounted price |
| description | TextField | Product description |
| brand | CharField(100) | Brand name |
| category | CharField | Saree / Casual Shirt / Mobile / Laptop |
| product_image | ImageField | Product photo |

### Cart
| Field | Type | Description |
|-------|------|-------------|
| user | ForeignKey(User) | Owner |
| product | ForeignKey(Product) | Product added |
| quantity | PositiveIntegerField | Quantity (default: 1) |

### OrderPlaced
| Field | Type | Description |
|-------|------|-------------|
| user | ForeignKey(User) | Customer |
| customer | ForeignKey(Customer) | Delivery address |
| product | ForeignKey(Product) | Product ordered |
| quantity | PositiveIntegerField | Quantity ordered |
| ordered_date | DateTimeField | Order timestamp |
| status | CharField | Accepted / Packed / On The Way / Delivered / Cancelled |

### Customer
| Field | Type | Description |
|-------|------|-------------|
| user | ForeignKey(User) | Linked user account |
| name | CharField(100) | Full name |
| locality | CharField(100) | Locality/area |
| city | CharField(100) | City |
| zipcode | IntegerField | PIN code |
| state | CharField | Indian state |

## URL Routes

| URL Prefix | App | Purpose |
|------------|-----|---------|
| `/admin/` | Django | Admin panel |
| `/product/` | product | Shopping pages (browse, cart, checkout, orders, search) |
| `/customer/` | customer | Auth, profile, password management |
| `/api/` | api | REST API endpoints |

### Product Routes
| Path | View | Name |
|------|------|------|
| `/product/` | ProductView | Product listing (home) |
| `/product/product/` | ProductSerialView | Product API data |
| `/product/product-detail/<pk>/` | ProductDetailView | Single product page |
| `/product/cart/` | add_to_cart | Add item to cart |
| `/product/buy/` | buy_now | Direct purchase |
| `/product/orders/` | orders | Order history |
| `/product/mobile/` | mobile | Mobile category filter |
| `/product/mobile/<data>/` | mobile | Mobile filter with data |
| `/product/checkout/` | checkout | Checkout page |
| `/product/search/` | search_page | Search results |
| `/product/autosuggest/` | auto_suggest | Search suggestions |

### Customer Routes
| Path | View | Name |
|------|------|------|
| `/customer/` | CustomerRegistrationView | Registration |
| `/customer/profile/` | profile | User profile |
| `/customer/address/` | address | Address management |
| `/customer/accounts/login/` | LoginView | Login |
| `/customer/logout/` | LogoutView | Logout |
| `/customer/registration/` | CustomerRegistrationView | Registration |
| `/customer/password-change/` | PasswordChangeView | Change password |
| `/customer/password-reset/` | PasswordResetView | Request reset |
| `/customer/password-reset-confirm/<uidb64>/<token>/` | PasswordResetConfirmView | Confirm reset |

## Setup

### Prerequisites
- Python 3.6+
- Redis (for Celery)
- A `.env` file with required environment variables

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/developer-tvc/WebMall.git
cd WebMall

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# Create a .env file in the project root:
# SECRET_KEY=<your-django-secret-key>
# EMAIL_HOST=<your-smtp-host>
# EMAIL_HOST_USER=<your-email>
# EMAIL_HOST_PASSWORD=<your-email-password>
# EMAIL_PORT=<smtp-port>

# 5. Run database migrations
python manage.py migrate

# 6. Create a superuser (optional, for admin access)
python manage.py createsuperuser
```

### Running the Application

```bash
# Start the Django development server
python manage.py runserver

# Start Celery worker (in a separate terminal)
celery -A WebMall worker -l info
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `EMAIL_HOST` | SMTP server hostname |
| `EMAIL_HOST_USER` | SMTP username |
| `EMAIL_HOST_PASSWORD` | SMTP password |
| `EMAIL_PORT` | SMTP port (default: 25) |

## License

This project is open source.
