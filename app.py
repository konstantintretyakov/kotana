from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    print(f"[Contact] Name: {name}, Phone: {phone}, Email: {email}")
    return render_template("index.html", success=True)


if __name__ == "__main__":
    app.run(debug=True)
