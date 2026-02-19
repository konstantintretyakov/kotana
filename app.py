from flask import Flask, render_template, Response

app = Flask(__name__)

SITE_URL = "https://kotana.com.ru"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sitemap.xml")
def sitemap():
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{SITE_URL}/</loc>
        <changefreq>monthly</changefreq>
        <priority>1.0</priority>
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
