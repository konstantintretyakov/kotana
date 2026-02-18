import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

SMTP_SERVER = "smtp.yandex.ru"
SMTP_PORT = 587
SMTP_LOGIN = os.environ.get("SMTP_LOGIN", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
RECIPIENT = "info@kotana.com.ru"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    subject = f"Новая заявка от {name}"
    body = f"Имя: {name}\nТелефон: {phone}\nEmail: {email}"

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = SMTP_LOGIN
    msg["To"] = RECIPIENT

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10) as server:
            server.starttls()
            server.login(SMTP_LOGIN, SMTP_PASSWORD)
            server.sendmail(SMTP_LOGIN, RECIPIENT, msg.as_string())
    except Exception as e:
        print(f"[Contact] Email send failed: {e}")
        return render_template("index.html", success=False)

    return render_template("index.html", success=True)


if __name__ == "__main__":
    app.run(debug=True)
