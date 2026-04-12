# Cleanup Commands for DreamHome Project

## 1. Delete All Python Cache Files (__pycache__)

```bash
# Delete all __pycache__ directories recursively
find . -type d -name __pycache__ -exec rm -rf {} +

# OR using a simpler approach
find . -type d -name __pycache__ | xargs rm -rf
```

## 2. Delete All Migration Files (Keep initial structure)

```bash
# Delete all migration files EXCEPT __init__.py in each app
find ./*/migrations -type f -name "*.py" ! -name "__init__.py" -delete

# OR delete specific migration files for each app
rm -f adminHome/migrations/000*.py
rm -f applicant/migrations/000*.py
rm -f builder/migrations/000*.py
rm -f officer/migrations/000*.py
rm -f Registration/migrations/000*.py
```

## 3. Combined Cleanup (Cache + Migrations)

```bash
# Remove all pycache directories
find . -type d -name __pycache__ -exec rm -rf {} +

# Remove all migration files (except __init__.py)
find ./*/migrations -type f -name "*.py" ! -name "__init__.py" -delete

# Remove old database
rm -f db.sqlite3
rm -f db.sqlite3-journal
```

## 4. Deep Cleanup (Everything except source code)

```bash
# Remove pycache
find . -type d -name __pycache__ -exec rm -rf {} +

# Remove Python compiled files
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.pyd" -delete

# Remove migration files
find ./*/migrations -type f -name "*.py" ! -name "__init__.py" -delete

# Remove database files
rm -f db.sqlite3 db.sqlite3-journal

# Remove Django logs
rm -f *.log

# Clear media uploads (be careful!)
# rm -rf media/*
```

## 5. Reset Migrations (Start Fresh)

After running the cleanup, regenerate migrations:

```bash
# Create migrations for all apps
python manage.py makemigrations

# Apply migrations to create database
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## Recommended Sequence

```bash
# 1. Stop the development server (if running)
# Ctrl+C

# 2. Delete cache and migrations
find . -type d -name __pycache__ -exec rm -rf {} +
find ./*/migrations -type f -name "*.py" ! -name "__init__.py" -delete

# 3. Remove old database
rm -f db.sqlite3 db.sqlite3-journal

# 4. Regenerate migrations
python manage.py makemigrations

# 5. Apply migrations
python manage.py migrate

# 6. Create new superuser
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver
```

## One-Liner Commands

```bash
# Clean everything
find . -type d -name __pycache__ -exec rm -rf {} + && find ./*/migrations -type f -name "*.py" ! -name "__init__.py" -delete && rm -f db.sqlite3 db.sqlite3-journal

# After cleanup, recreate migrations and database
python manage.py makemigrations && python manage.py migrate
```
