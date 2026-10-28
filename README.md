# Watchmate

Watchmate is a small Django and Django REST Framework learning project for a movie watchlist. It defines a `Movie` model with a name, description, and active status. The movie-list view and API behavior are still under development.

## Requirements

- Python 3
- Django
- Django REST Framework

## Setup

1. Clone the repository and open its directory.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   python -m pip install Django djangorestframework
   ```

4. Generate a development secret key and set it in the current PowerShell session:

   ```powershell
   $env:DJANGO_SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. Apply database migrations and start the development server:

   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```

The project is configured for local development. Set `DJANGO_SECRET_KEY` securely in the deployment environment and review Django's deployment checklist before deploying.

## Project layout

- `watchmate/` — Django project configuration and root URL routes.
- `watchlist_app/` — Movie model, app routes, and migrations.

The app's movie-list route is `/movie/list/`; its view is currently a work in progress.
