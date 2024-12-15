from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Login route that handles both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Validate credentials
        if username == "admin" and password == "admin123":
            return redirect(url_for("dashboard"))  # Redirect to the dashboard if login is successful
        return "Invalid Credentials!"  # Show an error if login fails
    
    # Render the login page on GET request
    return render_template("login.html")

# Dashboard route that renders the dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")  # Render the dashboard template

if __name__ == "__main__":
    app.run(debug=True)
