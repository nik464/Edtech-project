Semiconductor EdTech Workshop Management

Quickstart

1. Setup

- Python 3.13 is installed. Create venv and install deps:

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

2. Run

```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Admin user: admin / admin12345

Features

- Public tabs for Upcoming, Live, Completed
- Search by topic, location, mode, dates
- Coordinator login; create/update their workshops
- Upload agenda PDF, photos, documents (PDF) with size limits
- Dashboard with year-wise counts, participants total, Excel/PDF export
- Mobile-friendly Bootstrap UI
