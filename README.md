# 🛒 Pinzo — Pinduoduo-style Marketplace (Iran)

یک فروشگاه اینترنتی با خرید گروهی، تخفیف پلکانی، کیف پول، کش‌بک لحظه‌ای و سیستم دعوت. ساخته‌شده برای بازار ایران.

## ✨ ویژگی‌ها
- 🛍️ خرید تکی با تخفیف پلکانی (Campaign)
- 👥 خرید گروهی (Group Buy) — قیمت عمده با چند نفر
- 💰 کیف پول با شارژ از درگاه و کش‌بک لحظه‌ای
- 🎁 سیستم دعوت و رفرال با لیدربرد
- 📱 اپلیکیشن موبایل (React Native + Expo)
- 🌐 پنل ادمین (React) با چند سطح دسترسی
- 🇮🇷 فارسی کامل، راست‌چین (RTL)
- ⚡ Real-time با WebSocket

## 🧱 معماری
- Backend: Django 5 + DRF + Channels
- Frontend (Web): React 18 + Vite + TypeScript + Tailwind + shadcn/ui
- Admin Panel: React 18 + Vite + TypeScript + Ant Design
- Mobile: React Native + Expo (TypeScript)
- Database: PostgreSQL 16
- Cache/Queue/WS: Redis 7
- Object Storage: MinIO
- Task Queue: Celery
- Reverse Proxy: Nginx + Let's Encrypt
- CI/CD: GitHub Actions
- Containerization: Docker + Docker Compose

## 📁 ساختار
- `backend/` — Django + DRF
- `frontend/` — React + Vite (کاربر)
- `admin-panel/` — React + Vite (ادمین)
- `mobile/` — React Native + Expo
- `infra/nginx/` — Nginx configs
- `.github/workflows/` — CI/CD
- `docker-compose.yml` / `docker-compose.dev.yml`

## 🚀 شروع سریع
```bash
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
cp admin-panel/.env.example admin-panel/.env
cp mobile/.env.example mobile/.env

docker compose -f docker-compose.dev.yml up -d --build
docker compose -f docker-compose.dev.yml exec backend python manage.py migrate
docker compose -f docker-compose.dev.yml exec backend python manage.py createsuperuser
```

## 📍 دسترسی‌ها
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/api/v1/
- API Docs (Swagger): http://localhost:8000/api/docs/
- Django Admin: http://localhost:8000/admin/
- React Admin: http://localhost:5174
- MinIO Console: http://localhost:9001
