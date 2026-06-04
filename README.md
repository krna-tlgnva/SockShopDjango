# SockShopDjango

SockShopDjango is an online sock store built with Django. The project demonstrates a basic e-commerce workflow: product catalog, product details, shopping cart, order flow, and an admin panel for managing store data.

## Features

- Product catalog for socks
- Product detail pages
- Shopping cart
- Order creation workflow
- Django admin panel
- Template-based frontend with HTML/CSS
- SQLite support for local development

## Tech Stack

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/KarinaTulegenova/SockShopDjango.git
cd SockShopDjango
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the project in your browser:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Project Structure

```text
SockShopDjango/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── templates/
├── static/
└── README.md
```

The exact structure may differ depending on the application modules used in the project.

## Common Commands

Run migrations:

```bash
python manage.py migrate
```

Create new migrations:

```bash
python manage.py makemigrations
```

Run the server:

```bash
python manage.py runserver
```

Run tests:

```bash
python manage.py test
```

## Environment Variables

For local development, the project can use Django defaults. For production, configure:

```text
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```



## Author

Karina Tulegenova

GitHub: [KarinaTulegenova](https://github.com/KarinaTulegenova)

## License

This project is created for educational purposes.
