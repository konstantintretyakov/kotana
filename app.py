from flask import Flask, render_template, Response
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
</urlset>"""
    return Response(xml, mimetype="application/xml")


@app.route("/robots.txt")
def robots():
    txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml"""
    return Response(txt, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
