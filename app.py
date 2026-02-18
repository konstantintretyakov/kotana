import os

import requests
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
RECIPIENT = "info@kotana.com.ru"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    try:
        resp = requests.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {RESEND_API_KEY}"},
            json={
                "from": "Kotana <onboarding@resend.dev>",
                "to": [RECIPIENT],
                "subject": f"Новая заявка от {name}",
                "text": f"Имя: {name}\nТелефон: {phone}\nEmail: {email}",
            },
            timeout=10,
        )
        resp.raise_for_status()
    except Exception as e:
        print(f"[Contact] Email send failed: {e}")
        return render_template("index.html", success=False)

    return render_template("index.html", success=True)


if __name__ == "__main__":
    app.run(debug=True)
