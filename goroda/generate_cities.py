# -*- coding: utf-8 -*-
"""
Генератор SEO-страниц «Снеговая нагрузка в <городе>» для сайта Stroniq.
═══════════════════════════════════════════════════════════════════════════
ВАЖНО: нормативные значения (снеговая зона, sk) я НЕ выдумываю.
Заполни словарь CITIES ниже значениями из своего модуля снега
(city-to-zone mapping в snow_core / cities) — и запусти:

    python generate_cities.py

Скрипт создаст goroda/snegovaya-nagruzka-<город>.html на каждый город
и выведет готовые строки для sitemap.xml.
═══════════════════════════════════════════════════════════════════════════
"""
import os
import re

# ── ЗАПОЛНИ ИЗ СВОЕГО МОДУЛЯ (значения ниже — ПУСТЫЕ ЗАГЛУШКИ) ──────────────
# slug — латиницей для URL. zone — номер/имя снегового района по карте 4.
# sk — характеристическое значение на грунте, кПа, по карте 4.
CITIES = {
    # "Алматы":     {"slug": "almaty",     "zone": "", "sk": None},
    # "Астана":     {"slug": "astana",     "zone": "", "sk": None},
    # "Караганда":  {"slug": "karaganda",  "zone": "", "sk": None},
    # "Павлодар":   {"slug": "pavlodar",   "zone": "", "sk": None},
    # ... добавь 15–20 городов из своего маппинга
}

SITE = "https://stroniq.com"
APP = "https://stroniq-constcalc.streamlit.app/"

PAGE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Снеговая нагрузка в {city}: снеговой район, sk, расчёт по СП РК EN 1991-1-3</title>
<meta name="description" content="Снеговая нагрузка для {city}: снеговой район {zone}, характеристическое значение sk = {sk} кПа. Расчёт нагрузки на кровлю по СП РК EN 1991-1-3 онлайн с отчётом.">
<link rel="canonical" href="{site}/goroda/snegovaya-nagruzka-{slug}.html">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>
<div class="sheet">
<header class="stamp">
  <div class="brand"><a href="../index.html">STRONIQ<span class="dot">.</span></a></div>
  <nav>
    <a href="../index.html#stati">Статьи</a>
    <a class="cta" href="{app}" rel="noopener">Открыть калькулятор</a>
  </nav>
</header>
<div class="inner">
<div class="breadcrumbs"><a href="../index.html">Главная</a> / Города / {city}</div>
<article>
<h1>Снеговая нагрузка в {city}</h1>
<div class="meta">СП РК EN 1991-1-3 · карта снегового районирования РК</div>
<table>
  <tr><th>Город</th><td>{city}</td></tr>
  <tr><th>Снеговой район (карта 4)</th><td>{zone}</td></tr>
  <tr><th>s<sub>k</sub> на грунте</th><td>{sk} кПа</td></tr>
</table>
<p>Характеристическое значение снеговой нагрузки на грунте для города {city} —
<strong>s<sub>k</sub> = {sk} кПа</strong> (снеговой район {zone} по карте районирования
национального приложения СП РК EN 1991-1-3).</p>
<p>Нагрузка на кровлю зависит от её формы: s = μ·C<sub>e</sub>·C<sub>t</sub>·s<sub>k</sub>.
Для плоской и пологой кровли (уклон до 30°) μ = 0,8, то есть базовое значение на кровле
для {city} — около <strong>{s_roof} кПа</strong> (равномерное загружение, обычная местность).
Для двускатных кровель дополнительно рассматриваются несимметричные схемы снегового мешка,
для перепадов высот и парапетов — локальные наносы.</p>
<div class="appbox">
  <p><strong>Полный расчёт для {city} — с формой кровли, схемами мешка, локальными
  эффектами и отчётом PDF/Word/Excel:</strong></p>
  <a class="btn primary" href="{app}" rel="noopener">Рассчитать снеговую нагрузку для {city} →</a>
</div>
<p>Методика расчёта с примером — в статье
<a href="../blog/raschet-snegovoy-nagruzki-sp-rk-en-1991-1-3.html">«Расчёт снеговой нагрузки
по СП РК EN 1991-1-3: пошаговый пример»</a>.</p>
<p><em>Значения приведены по действующей редакции СП РК EN 1991-1-3 с национальным
приложением; при проектировании сверяйтесь с нормативом.</em></p>
</article>
</div>
<footer class="stamp">
  <div class="row">
    <div class="cell"><span class="lbl">Проект</span>Stroniq — сбор нагрузок по СП РК EN</div>
    <div class="cell"><span class="lbl">Раздел</span>Города · {city}</div>
    <div class="cell"><span class="lbl">Калькулятор</span><a href="{app}" rel="noopener">открыть →</a></div>
  </div>
</footer>
</div>
</body>
</html>
"""

def main():
    if not CITIES:
        print("Словарь CITIES пуст. Заполни его значениями зоны и sk из своего "
              "модуля снега (нормативные данные — только из норматива!) и запусти снова.")
        return
    outdir = os.path.dirname(os.path.abspath(__file__))
    sitemap_lines = []
    for city, d in CITIES.items():
        if not d.get("zone") or d.get("sk") is None:
            print(f"⚠️ {city}: нет zone/sk — пропущен")
            continue
        s_roof = round(0.8 * float(d["sk"]), 2)
        html = PAGE.format(city=city, slug=d["slug"], zone=d["zone"],
                           sk=d["sk"], s_roof=s_roof, site=SITE, app=APP)
        fname = f"snegovaya-nagruzka-{d['slug']}.html"
        with open(os.path.join(outdir, fname), "w", encoding="utf-8") as f:
            f.write(html)
        sitemap_lines.append(f"  <url><loc>{SITE}/goroda/{fname}</loc></url>")
        print(f"✅ {city} → goroda/{fname}")
    print("\nДобавь в sitemap.xml перед </urlset>:")
    print("\n".join(sitemap_lines))

if __name__ == "__main__":
    main()
