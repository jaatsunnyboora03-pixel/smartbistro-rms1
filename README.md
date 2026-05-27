# SmartBistro — Restaurant Management System
> SENG205 Software Engineering · Kent Institute Australia · T1 2026

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Django](https://img.shields.io/badge/Django-5.0-green) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue) ![Docker](https://img.shields.io/badge/Docker-Compose-informational)

## Project Overview
SmartBistro is a next-generation Restaurant Management System for high-volume urban eateries. It unifies QR-based ordering, real-time Kitchen Display System (KDS), inventory management, and analytics into a single Django/PostgreSQL platform.

## Team Members
| Name  Role |
|------|------|
| [sunny] | [k231990 | Lead Developer / Backend |
| [Omor Rahad Shuvo] | Frontend / React |
| [S M Sadman Shahriyar Sad] | Backend / Inventory Module |
| [TROUNG TRAN] | UI/UX / Testing |

## Tech Stack
- **Backend:** Python 3.11, Django 5.0, Django REST Framework
- **Real-time:** Django Channels 4.0, Redis 7.0
- **Database:** PostgreSQL 16
- **Frontend:** React 18, Axios
- **Testing:** Pytest, Selenium 4
- **DevOps:** Docker, Docker Compose, GitHub Actions

---

## Sprint Plan
| Sprint | Weeks | Focus |
|--------|-------|-------|
| Sprint 1 | Wk 1–2 | Project setup, Docker, DB schema, CI pipeline |
| Sprint 2 | Wk 3–4 | QR ordering API, floor plan WebSocket |
| Sprint 3 | Wk 5–6 | KDS, order prioritisation, dietary alerts |
| Sprint 4 | Wk 7–8 | Inventory engine, race condition handling |
| Sprint 5 | Wk 9–10 | Reservations, payments, loyalty |
| Sprint 6 | Wk 11–12 | Analytics, E2E testing, deployment |

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-org>/smartbistro-rms.git
cd smartbistro-rms
```

### 2. Install dependencies
```bash
pip install -r backend/requirements.txt
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Start the server
```bash
python manage.py runserver
```

---

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/menu/` | List available menu items |
| POST | `/api/v1/orders/` | Create order |
| GET | `/api/v1/tables/` | List all tables with status |
| PATCH | `/api/v1/tables/{id}/` | Update table status |
| GET | `/api/v1/inventory/` | List ingredients with stock levels |
| POST | `/api/v1/reservations/` | Create reservation |
| GET | `/api/v1/analytics/dashboard/` | Summary stats |

---

## License
Kent Institute Australia — Academic Project, T1 2026
