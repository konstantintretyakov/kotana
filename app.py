from flask import Flask, render_template, Response, send_from_directory
from flask_compress import Compress

app = Flask(__name__)
Compress(app)

SITE_URL = "https://kotana.com.ru"


@app.route("/")
def index_ru():
    return render_template("index.html", lang="ru")


@app.route("/en/")
def index_en():
    return render_template("index.html", lang="en")


@app.route("/blog/ma-market-2025")
def blog_ma_market_2025():
    return render_template("blog/ma-market-2025.html")


@app.route("/blog/ma-market-2026-forecast")
def blog_ma_market_2026_forecast():
    return render_template("blog/ma-market-2026-forecast.html")


@app.route("/blog/corporate-lending-2025")
def blog_corporate_lending_2025():
    return render_template("blog/corporate-lending-2025.html")


@app.route("/blog/corporate-lending-2026-forecast")
def blog_corporate_lending_2026_forecast():
    return render_template("blog/corporate-lending-2026-forecast.html")


@app.route("/blog/china-fdi-russia-2025")
def blog_china_fdi_russia_2025():
    return render_template("blog/china-fdi-russia-2025.html")


@app.route("/blog/foreign-companies-return-forecast-2026")
def blog_foreign_companies_return_forecast_2026():
    return render_template("blog/foreign-companies-return-forecast-2026.html")


@app.route("/blog/ppp-market-russia-2025")
def blog_ppp_market_russia_2025():
    return render_template("blog/ppp-market-russia-2025.html")


@app.route("/blog/ppp-market-russia-2026-forecast")
def blog_ppp_market_russia_2026_forecast():
    return render_template("blog/ppp-market-russia-2026-forecast.html")


@app.route("/sitemap.xml")
def sitemap():
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
    <url>
        <loc>{SITE_URL}/</loc>
        <xhtml:link rel="alternate" hreflang="ru" href="{SITE_URL}/"/>
        <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/en/"/>
        <changefreq>monthly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{SITE_URL}/en/</loc>
        <xhtml:link rel="alternate" hreflang="ru" href="{SITE_URL}/"/>
        <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/en/"/>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>{SITE_URL}/blog/ma-market-2025</loc>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{SITE_URL}/blog/ma-market-2026-forecast</loc>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{SITE_URL}/blog/corporate-lending-2025</loc>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{SITE_URL}/blog/corporate-lending-2026-forecast</loc>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{SITE_URL}/blog/china-fdi-russia-2025</loc>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{SITE_URL}/blog/foreign-companies-return-forecast-2026</loc>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{SITE_URL}/blog/ppp-market-russia-2025</loc>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>{SITE_URL}/blog/ppp-market-russia-2026-forecast</loc>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
</urlset>"""
    return Response(xml, mimetype="application/xml")


@app.route("/favicon.svg")
def favicon_svg():
    return send_from_directory(app.static_folder, "favicon.svg", mimetype="image/svg+xml")


@app.route("/favicon.ico")
def favicon_ico():
    return send_from_directory(app.static_folder, "favicon.ico", mimetype="image/x-icon")


@app.route("/favicon.png")
def favicon_png():
    return send_from_directory(app.static_folder, "favicon.png", mimetype="image/png")


@app.route("/robots.txt")
def robots():
    txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml"""
    return Response(txt, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
