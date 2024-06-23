import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'
login_manager.login_message_category = 'info'
csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        users = get_users()
        for user in users:
            if user['id'] == user_id:
                return User(user['id'], user['username'], user['email'], user['password'])
        return None

def get_users():
    return [
        {
            "id": "1",
            "username": "admin",
            "email": "admin@example.com",
            "password": generate_password_hash("adminpassword")
        }
    ]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
@csrf.exempt
def search():
    query = request.form.get('query') if request.method == 'POST' else request.args.get('query')
    if not query:
        flash('Please provide a search query.', 'danger')
        return redirect(url_for('home'))

    page = int(request.args.get('page', 1))
    per_page = 10  
    results = search_files(query)
    paginated_results = results[(page - 1) * per_page:page * per_page]  
    total_pages = (len(results) + per_page - 1) // per_page 
    return render_template('results.html', query=query, results=paginated_results, page=page, total_pages=total_pages)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

def search_files(query):
    results = []
    for root, dirs, files in os.walk('data'):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, start=1):
                    if query.lower() in line.lower():
                        result = {
                            'file': file,
                            'line_number': line_num,
                            'line': line.strip()
                        }
                        results.append(result)
    return results

if __name__ == '__main__':
    app.run(debug=True)

