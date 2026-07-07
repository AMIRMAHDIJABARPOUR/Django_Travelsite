# Django Weblog

A Django-based blog application with authentication, content management, search, comments, RSS feeds, sitemap, robots.txt, and SEO-related features.

This project focuses on backend development with Django and integrates a pre-built HTML, CSS, and JavaScript template with Django models, views, templates, static files, and media files.

## Overview

Django Weblog is a portfolio project built to practice core Django concepts such as models, views, templates, forms, authentication, admin customization, search, pagination, comments, static/media file handling, RSS feeds, sitemap generation, and production-ready configuration.

The project uses separate settings for development and production environments.

## Project Advantages

- Complete Django-based blog structure
- Clean separation between backend logic and frontend templates
- Content management through Django Admin
- Integration of authentication, search, comments, RSS feed, sitemap, and robots.txt
- Separate development and production settings
- SQLite for local development
- PostgreSQL configuration for production
- Environment-based configuration for sensitive production settings
- Responsive pre-built frontend template integrated with Django

## Features

- User registration, login, and logout
- Blog post creation and management through Django Admin
- Post detail pages
- Post categories
- Post tags using `django-taggit`
- Search functionality
- Pagination
- Comment submission with admin approval
- Image uploads for blog posts
- Static and media file management
- RSS feed for latest posts
- Dynamic XML sitemap
- robots.txt management
- CAPTCHA support
- Django Debug Toolbar in development
- Responsive frontend template integration

## Tech Stack

- Python
- Django
- Django Templates
- SQLite for development
- PostgreSQL for production
- HTML
- CSS
- JavaScript
- Pillow
- django-taggit
- django-robots
- django-simple-captcha
- django-multi-captcha-admin
- django-debug-toolbar
- python-decouple

## Development and Production Settings

This project is configured with separate settings for development and production.

### Development

The development environment uses:

- `DEBUG=True`
- SQLite database
- Django Debug Toolbar
- Local static and media file handling
- Non-secure cookies for local development

Development settings are intended only for local testing and should not be used in production.

### Production

The production environment uses:

- Environment variables for sensitive settings
- PostgreSQL database
- Secure cookie settings
- HTTPS-related security configuration
- Separate static and media file paths
- Email configuration through environment variables

Before deploying to production, make sure all required environment variables are configured properly.

## Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/AMIRMAHDIJABARPOUR/Django_Weblog
cd Django_Weblog
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file for sensitive settings.

Example for production:

```env
DEBUG=False
SECRET_KEY=your-production-secret-key

DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=your-database-host
DB_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-email-password
```

Do not commit the real `.env` file, production secrets, database credentials, or email passwords to GitHub.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open the project in your browser:

```text
http://127.0.0.1:8000/
```

## Useful URLs

```text
Admin Panel:  http://127.0.0.1:8000/admin/
RSS Feed:     http://127.0.0.1:8000/rss/
Sitemap:      http://127.0.0.1:8000/sitemap.xml
robots.txt:   http://127.0.0.1:8000/robots.txt
```

## Project Structure

```text
Django_Weblog/
├── Config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
│
├── blog_page/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── feeds.py
│   ├── sitemaps.py
│   └── templatetags/
│
├── accounts/
├── home_page/
├── templates/
├── static/
├── media/
├── requirements.txt
├── manage.py
└── README.md
```

## Notes

- The frontend template was pre-built and integrated with Django.
- The backend logic, database integration, authentication, blog functionality, search, pagination, comments, RSS feed, sitemap, and robots.txt configuration were implemented in Django.
- Comments are submitted by users and displayed only after admin approval.
- The development environment uses SQLite and Django Debug Toolbar.
- The production environment is configured for PostgreSQL and secure settings through environment variables.
- `media/`, `staticfiles/`, `.env`, and `db.sqlite3` should not be committed to GitHub.

## Security Notes

- Development settings are only for local development.
- Production settings load sensitive values from environment variables.
- `SECRET_KEY`, database credentials, and email credentials must not be committed to GitHub.
- `DEBUG` must be set to `False` in production.
- Secure cookie settings are enabled in production.
- SQLite is used for local development, while PostgreSQL is used for production.

## Project Highlights

- Integrated a pre-built responsive frontend template with Django views, models, templates, static files, and media files.
- Implemented blog posts, categories, tags, search, pagination, comments, RSS feed, sitemap, and robots.txt support.
- Managed blog content through Django Admin with image upload and post metadata.
- Added separate development and production settings for local testing and production deployment.
- Configured comment moderation through admin approval.

## Future Improvements

- Add automated tests for blog views, search, comments, and authentication.
- Add a custom author dashboard for creating and editing posts outside Django Admin.
- Improve comment moderation and spam protection.
- Add richer SEO metadata for blog posts.
- Add deployment instructions for the production environment.

## Project Purpose

This project was developed for learning and portfolio purposes.
