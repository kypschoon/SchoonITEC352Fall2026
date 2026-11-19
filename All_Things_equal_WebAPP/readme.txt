All Things Equal - Django Web Application
ITEC 352 Final Project

HOW TO RUN THE APPLICATION FROM VS CODE
========================================

1. Open the project folder in VS Code:
   C:\Users\Path...

2. Open a terminal in VS Code (Terminal → New Terminal).

3. Activate the virtual environment (if it is not already active):
   .\.venv\Scripts\Activate.ps1

4. Make sure dependencies are installed:
   pip install django pillow

5. Apply database migrations (only needed the first time or after model changes):
   python manage.py migrate

6. Start the development server:
   python manage.py runserver

7. Open a browser and go to:
   http://127.0.0.1:8000/

ADMIN ACCESS
============
- Go to http://127.0.0.1:8000/admin/
- Log in with the superuser account you created.
- From the admin you can add/edit Pricing Plans, Reviews, and view Quote Requests.

PAGES
=====
- Home:          http://127.0.0.1:8000/
- About:         http://127.0.0.1:8000/about/
- Pricing:       http://127.0.0.1:8000/pricing/
- Reviews:       http://127.0.0.1:8000/reviews/
- Request Quote: http://127.0.0.1:8000/quote/

NOTES
=====
- Quote form emails are printed in the terminal for now.
- The database is SQLite.
- Project structure:
  - config/     (settings and main urls)
  - core/       (models, views, forms, admin, templates)
  - manage.py
  - db.sqlite3
