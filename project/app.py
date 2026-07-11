from flask import Flask, render_template, request, redirect, url_for, session, send_file
import sqlite3, csv
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret-key"

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_db()
    expenses = conn.execute("SELECT * FROM expenses WHERE user_id=?", (session["user_id"],)).fetchall()
    total = conn.execute("SELECT SUM(amount) as total FROM expenses WHERE user_id=?", (session["user_id"],)).fetchone()["total"]
    return render_template("dashboard.html", expenses=expenses, total_amount=total or 0)

@app.route("/add", methods=["POST"])
def add():
    if "user_id" not in session:
        return redirect(url_for("login"))
    category = request.form["category"]
    amount = request.form["amount"]
    conn = get_db()
    conn.execute("INSERT INTO expenses (category, amount, user_id) VALUES (?, ?, ?)", (category, amount, session["user_id"]))
    conn.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM expenses WHERE id=? AND user_id=?", (id, session["user_id"]))
    conn.commit()
    return redirect("/")

@app.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    category = request.form["category"]
    amount = request.form["amount"]
    conn = get_db()
    conn.execute("UPDATE expenses SET category=?, amount=? WHERE id=? AND user_id=?", (category, amount, id, session["user_id"]))
    conn.commit()
    return redirect("/")

@app.route("/export")
def export():
    conn = get_db()
    expenses = conn.execute("SELECT * FROM expenses WHERE user_id=?", (session["user_id"],)).fetchall()
    with open("expenses.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Category", "Amount", "Date"])
        for e in expenses:
            writer.writerow([e["id"], e["category"], e["amount"], e["date"]])
    return send_file("expenses.csv", as_attachment=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            return redirect("/")
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = generate_password_hash(request.form["password"])
    conn = get_db()
    conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    return redirect("/login")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
