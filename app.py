
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("registration.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    course = request.form.get("course", "").strip()

    return render_template(
        "success.html",
        name=name,
        email=email,
        phone=phone,
        course=course
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
