# todo_project

Simple Django To-Do App ready for deployment on Render.

## Quick start (locally)

1. Create virtual env and install:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run migrations and start dev server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

3. Create a superuser to access admin:
   ```bash
   python manage.py createsuperuser
   ```

## Deploy to Render

1. Push this repo to GitHub.
2. On Render, create a new **Web Service** from your repo.
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn todo_project.wsgi --log-file -`
3. Optionally set `DEBUG=False` and replace `SECRET_KEY` in production.

