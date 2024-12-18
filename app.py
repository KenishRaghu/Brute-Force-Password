from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin":
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials!!"
    else:
        return render_template("login.html")

@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)  

