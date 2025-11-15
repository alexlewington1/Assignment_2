# Ipswich Retail — E-commerce Django Website

This repository contains a small Django-based e-commerce website for a fictional store called Ipswich Retail. The project provides a landing page, product page, and informational pages (About Us and Contact Us), and is organized as a Django project named `ecommerce` with a single app `Ipswich_Retail`.

**Primary features**
- Simple landing page with static assets (HTML/CSS/JS).
- Product page template for listing or showing product details.
- About Us and Contact Us informational pages.
- Uses SQLite (`db.sqlite3`) for local development.

Project structure (key files/folders):
- `manage.py`: Django management entrypoint.
- `ecommerce/`: Django project configuration.
- `Ipswich_Retail/`: Django app containing views, templates, static files, and migrations.
- `db.sqlite3`: Local SQLite database (development).

Quick setup (development)

1. Create a Python virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies. If there is no `requirements.txt`, install Django (tested with Django 4.x) and any other packages you need:

```bash
pip install Django
```

3. Run migrations (the repo already contains `db.sqlite3`, but to recreate or update the DB):

```bash
python manage.py migrate
```

4. (Optional) Create a superuser to access the admin site:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

Notes for contributors
- Templates are in `Ipswich_Retail/templates/` (examples: `LandingPage.html`, `ProductPage.html`, `AboutUs.html`, `ContactUs.html`).
- Static assets are in `Ipswich_Retail/static/` (CSS/JS/images).
- To add products or dynamic data, extend models in `Ipswich_Retail/models.py` and update views/templates accordingly.

Testing and checks
- There is a `tests.py` file in `Ipswich_Retail/` — run tests with:

```bash
python manage.py test
```

License & attribution
- This project is a small assignment/demonstration and does not include a license file. Add a `LICENSE` if you plan to distribute it.

Contact
- If you need help running the project or want me to add a `requirements.txt` and CI/test workflow, tell me and I can add them.
