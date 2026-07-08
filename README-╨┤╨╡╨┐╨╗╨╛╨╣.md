# Как задеплоить сайт Stroniq (GitHub Pages, бесплатно)

## Шаг 1. Новый репозиторий
1. В GitHub Desktop: File → New repository → имя `stroniq-site`.
2. Скопируй в папку репозитория ВСЁ содержимое папки site/
   (index.html, css/, blog/, goroda/, sitemap.xml, robots.txt).
3. Commit → Publish repository (públic).

## Шаг 2. Включить Pages
1. github.com → репозиторий stroniq-site → Settings → Pages.
2. Source: Deploy from a branch → Branch: main → / (root) → Save.
3. Через 1–2 мин сайт живёт на https://ТВОЙ_ЛОГИН.github.io/stroniq-site/

## Шаг 3. Свой домен (сильно желательно для SEO)
1. Купи stroniq.kz (или .app) у регистратора (ps.kz, hoster.kz — от ~2000 ₸/год за .kz).
2. В Settings → Pages → Custom domain впиши stroniq.kz.
3. У регистратора добавь DNS-записи, которые покажет GitHub (A-записи + CNAME www).
4. Дождись галочки Enforce HTTPS.

## Шаг 4. Google Search Console (обязательный шаг для выхода в поиск)
1. search.google.com/search-console → Добавить ресурс → домен stroniq.kz.
2. Подтверди владение (DNS-записью TXT — регистратор поможет).
3. Отправь sitemap: в меню «Файлы Sitemap» → https://stroniq.kz/sitemap.xml
4. Проверь через неделю «Покрытие» — страницы должны попасть в индекс.

## Шаг 5. Города
1. Открой goroda/generate_cities.py, заполни CITIES значениями зоны и sk
   из своего модуля снега (только нормативные значения!).
2. python generate_cities.py — создаст страницы и напечатает строки для sitemap.
3. Вставь строки в sitemap.xml, закоммить, запушь.

## Если в ссылках калькулятора появится свой поддомен
Захочешь app.stroniq.kz вместо streamlit.app — это отдельная настройка
(Streamlit Cloud поддерживает custom subdomain через CNAME). Не обязательно
для старта: ссылки на streamlit.app работают.
