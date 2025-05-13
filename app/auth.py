from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth = Blueprint('auth', __name__)

# בסיס נתונים זמני בזיכרון
users = {}

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash("Username already exists")
            return redirect(url_for('auth.register'))
        users[username] = password
        flash("Registered successfully. Please login.")
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            flash("Logged in successfully")
            return redirect(url_for('main.index'))
        else:
            flash("Invalid credentials")
            return redirect(url_for('auth.login'))
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out")
    return redirect(url_for('main.index'))

