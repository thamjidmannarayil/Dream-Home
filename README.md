# DreamHome - Property Management System

A Django-based web application for managing property projects, builder registrations, applicant requests, and quotations.

## Project Overview

DreamHome is a comprehensive property management platform that facilitates communication between property officers, builders, and applicants. The system handles:

- **Property Projects**: Creation and management of housing projects
- **Builder Management**: Registration and tracking of builders and their quotations
- **Applicant Requests**: Processing applications from property seekers
- **Quotations**: Managing builder quotations for projects
- **Complaints & Reports**: Handling complaints and survey reports
- **Plot Management**: Tracking available plots and their details

## Features

- User authentication and role-based access control
- Project and plot management system
- Quotation and bidding system for builders
- Complaint management system
- Survey report generation
- District and village-based location tracking
- File upload support for documents and images

## Project Structure

```
dreamHome/
├── adminHome/          # Admin dashboard and core models
├── applicant/          # Applicant registration and requests
├── builder/            # Builder registrations and quotations
├── officer/            # Officer functionality and project management
├── registration/       # User registration system
├── dreamHome/          # Project settings and configuration
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
└── README.md          # This file
```

## Tech Stack

- **Framework**: Django 5.0+
- **Database**: SQLite (development), MySQL (production-ready)
- **Python**: 3.12+
- **Frontend**: HTML/CSS/JavaScript (in templates)

## Installation

### Prerequisites

- Python 3.12+
- pip (Python package manager)
- Virtual environment support

### Setup Instructions

1. **Clone or navigate to the project directory**
   ```bash
   cd /mnt/d/Personal/dreamHome/dreamHome
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env-dreamhome
   source env-dreamhome/bin/activate  # On Windows: env-dreamhome\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your settings
   nano .env
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

   The application will be available at: `http://localhost:8000`

## Environment Configuration

The project uses `.env` file for configuration management. This file is **NOT** committed to version control for security reasons.

### Setting Up .env File

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your configuration:
   ```bash
   DEBUG=True
   SECRET_KEY=your-secret-key-change-in-production
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_ENGINE=django.db.backends.sqlite3
   ```

### Environment Variables

#### Django Settings
- `DEBUG` - Set to False in production
- `SECRET_KEY` - Django secret key (change in production)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts

#### Database Configuration
- `DB_ENGINE` - Database backend (sqlite3 or mysql)
- `DB_NAME` - Database name
- `DB_USER` - Database user (MySQL only)
- `DB_PASSWORD` - Database password (MySQL only)
- `DB_HOST` - Database host (MySQL only)
- `DB_PORT` - Database port (MySQL only)

#### Optional Settings
- `EMAIL_HOST` - SMTP server
- `EMAIL_PORT` - SMTP port
- `EMAIL_USE_TLS` - Use TLS for email
- `EMAIL_HOST_USER` - Email account
- `EMAIL_HOST_PASSWORD` - Email password
- `TIME_ZONE` - Application timezone
- `LANGUAGE_CODE` - Default language

See `.env.example` for all available options.

## Available Apps

### adminHome
- Core admin functionality
- Designation, district, and village management
- Quote types and office management
- FAQ management
- Role-based access control

### Registration
- User registration system
- Builder registration
- Applicant registration

### applicant
- Applicant request management
- Complaint handling
- Request tracking and status management

### officer
- Project management
- Plot management
- Quotation notifications
- Complaint reports
- Survey reports

### builder
- Builder quotation applications
- Bidding system for projects
- Builder documentation

## Management Commands

```bash
# Create migrations for model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create a superuser account
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access Django admin panel
# Navigate to /admin after starting the server

# Check project for errors
python manage.py check

# Collect static files (for production)
python manage.py collectstatic
```

## Admin Panel

Access the Django admin interface at:
```
http://localhost:8000/admin
```

Log in with your superuser credentials to manage:
- Users and permissions
- Projects and plots
- Quotations and bids
- Complaints and reports
- All database models

## Known Issues & Fixes Applied

✅ **Fixed Issues:**
- Circular imports between models resolved
- Wrong import statement in officer/views.py corrected
- Migration conflicts resolved (duplicate table definitions)
- Database configuration optimized for development

## Troubleshooting

### Migration Errors
If you encounter migration errors, try:
```bash
python manage.py migrate --fake-initial
```

### Database Connection Issues
- Ensure SQLite file has proper permissions
- For MySQL, verify credentials and services are running
- Check that MySQL Docker container is running (if using Docker)

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

## Development Notes

- Use `DEBUG = True` in `settings.py` for development
- Database uses SQLite by default for quick setup
- All migrations have been applied successfully
- Models are fully defined and ready for use

## Version Control

### .gitignore

The project includes a `.gitignore` file that excludes:
- Virtual environment directories
- Python cache and compiled files (`__pycache__/`, `*.pyc`)
- Database files (`db.sqlite3`)
- Environment files (`.env`)
- IDE/editor files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)
- Uploaded media files

### Important Files NOT in Git

- `.env` - Contains sensitive configuration (passwords, secret keys)
- `db.sqlite3` - Development database
- `env-dreamhome/` - Virtual environment

Always use `.env.example` to document required environment variables.

## Security Checklist for Production

Before deploying to production:

1. **Update .env**
   ```
   DEBUG=False
   SECRET_KEY=generate-a-new-secure-key
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   SECURE_SSL_REDIRECT=True
   SESSION_COOKIE_SECURE=True
   CSRF_COOKIE_SECURE=True
   ```

2. **Generate a new SECRET_KEY**
   ```bash
   python manage.py shell
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

3. **Run security checks**
   ```bash
   python manage.py check --deploy
   ```

4. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

5. **Switch to MySQL** for better performance and reliability


- API endpoints for mobile application support
- Advanced reporting and analytics
- Email notifications system
- Real-time project updates
- Payment gateway integration

## Contact & Support

For issues or questions about this project, refer to the project documentation or contact the development team.

## License

This project is proprietary and intended for authorized use only.
